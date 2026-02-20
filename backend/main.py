from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from ultralytics import YOLO
import os
import cv2
import hashlib

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("yolov8n.pt")

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_image_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()


@app.post("/detect")
async def detect_object(file: UploadFile = File(...), db: Session = Depends(get_db)):

    file_bytes = await file.read()
    image_hash = generate_image_hash(file_bytes)

    existing_detection = db.query(models.Detection)\
        .filter(models.Detection.image_hash == image_hash)\
        .first()

    cached_output_path = os.path.join(
        OUTPUT_FOLDER,
        f"{image_hash}_output.jpg"
    )

    if existing_detection and os.path.exists(cached_output_path):
        print("Returning cached result")
        return FileResponse(cached_output_path, media_type="image/jpeg")

    input_path = os.path.join(UPLOAD_FOLDER, f"{image_hash}.jpg")

    with open(input_path, "wb") as buffer:
        buffer.write(file_bytes)

    results = model(input_path)
    result = results[0]

    for box in result.boxes:
        class_id = int(box.cls[0])
        object_name = model.names[class_id]
        confidence = float(box.conf[0])

        detection = models.Detection(
            image_hash=image_hash,
            image_name=f"{image_hash}.jpg",
            object_name=object_name,
            confidence=confidence
        )
        db.add(detection)

    db.commit()

    result_img = result.plot()
    cv2.imwrite(cached_output_path, result_img)

    return FileResponse(cached_output_path, media_type="image/jpeg")
