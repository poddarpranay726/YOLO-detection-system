from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    image_hash = Column(String, index=True)
    image_name = Column(String, nullable=False)
    object_name = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
