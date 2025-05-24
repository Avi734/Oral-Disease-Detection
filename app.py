import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template, jsonify, send_from_directory
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

# Load trained model
print(tf.__version__)
print("NumPy version:", np.__version__)
print("Fals:",Flask.__version__)
MODEL_PATH = "My Coding done for Pandu Gaaru/resnet100.h5"
model = tf.keras.models.load_model(MODEL_PATH, compile=False)  # Load without compiling if needed
# model.summary()

# Define class labels (Update with your own classes)
CLASS_NAMES = ['calculus', 'caries', 'gingivitis', 'hypodontia', 'toothDiscoloration', 'ulcers']

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def predict_disease(image_path):
    """Preprocess image and predict disease"""
    img = load_img(image_path, target_size=(128, 128))  # Resize to match model input
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    predictions = model.predict(img_array)[0]
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = round(100 * np.max(predictions), 2)

    return predicted_class, confidence

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    # Save file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Predict disease
    predicted_class, confidence = predict_disease(filepath)

    return jsonify({
        "disease": predicted_class, 
        "confidence": confidence, 
        "image_url": f"/uploads/{file.filename}"
    })

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
