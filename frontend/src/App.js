import React, { useState } from "react";
import axios from "axios";

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [outputImage, setOutputImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedImage) return;

    const formData = new FormData();
    formData.append("file", selectedImage);

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/detect",
        formData,
        { responseType: "blob" }
      );

      const imageUrl = URL.createObjectURL(response.data);
      setOutputImage(imageUrl);
    } catch (err) {
      setError(err.response?.data?.detail || "Error processing image. Check backend.");
      console.error("Error:", err);
    }

    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "40px" }}>
      <h2>YOLO Object Detection</h2>

      <input type="file" onChange={handleImageChange} />
      <br /><br />

      <button onClick={handleUpload}>Detect Objects</button>

      {error && <p style={{ color: "red" }}>Error: {error}</p>}
      {loading && <p>Processing...</p>}

      {outputImage && (
        <div>
          <h3>Detected Output</h3>
          <img src={outputImage} alt="Detected" width="500" />
        </div>
      )}
    </div>
  );
}

export default App;
