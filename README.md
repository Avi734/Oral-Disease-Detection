# 🦷 Oral Disease Detection Using Smartphone-Based Images

A deep learning-based system designed to detect common oral diseases—such as caries, gingivitis, ulcers, hypodontia, tooth discoloration, and calculus—from smartphone images.
The system integrates multiple CNN architectures and provides a user-friendly Flask web app for real-time diagnosis.

---

## 🚀 Key Features

- 📷 **Smartphone-Compatible Image Input**  
  Upload images of your oral cavity for instant analysis.

- 🤖 **AI-Based Disease Classification**  
  Trained deep learning models (VGG16, ResNet101, DenseNet121, InceptionV3, VGG19, etc) for accurate detection.

- 💬 **Model Feedback**  
  Displays disease prediction along with confidence scores.

- 🌐 **Flask Web Application**  
  Simple, browser-based interface for ease of use on both mobile and desktop.

---


## 📁 Dataset

- **Source**: Custom-curated and annotated image dataset  
- **Size**: 13,862 high-resolution images  
- **Classes**: Caries, Gingivitis, Ulcers, Hypodontia, Tooth Discoloration, Calculus  
- **Split**: 70% Train, 15% Validation, 15% Test  
- **Preprocessing**: Resizing, normalization, augmentation (rotation, flipping, zoom)

---
🧠 Model
CNN-based architecture using Transfer Learning
Loss Function: categorical_crossentropy
Metrics: Accuracy, Precision, Recall, F1-score
Target Accuracy: ~95% with F1-score close to 1
---

## 📊 Evaluation Metrics

- **Accuracy**, **Precision**, **Recall**, **F1-Score**, **AUC**
- **Class imbalance** handled using:
  - Data augmentation
  - Class weights
  - Learning rate scheduling
  - Early stopping and regularization (L2, Dropout)

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, TensorFlow, Keras
- **Frontend**: HTML, CSS
- **Image Processing**: OpenCV, PIL
- **Visualization**: Matplotlib, Seaborn
  

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/Avi734/Oral-Disease-Detection.git

```
2. **Install Dependencies**
```bash
pip install -r requirements.txt
```
3. **Run the application**
```bash
python app.py
```
4. ** Open your browser and go to:**
http://localhost:5000

---
📊 **Evaluation**
VGG16: ~96.22 accuracy

Consistently high F1-score across all disease classes

ROC, Confusion Matrix, and classification reports used for detailed evaluation

----
🔮 Future Scope
1. Native mobile app integration

2. Broader disease coverage (e.g., oral cancer)

3. Multilingual support and voice-guided UI

4. Cloud deployment for real-time scalability

5. Real-time detection from video input

6. Clinical integration for remote dental screening

