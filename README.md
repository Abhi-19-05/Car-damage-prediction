# 🚗 Vehicle Damage Detection App

An AI-powered Vehicle Damage Detection application that predicts the type of damage present in a vehicle image.

The application allows users to upload a car image and uses a deep learning model to classify the damage category. The model performs best on **third-quarter front and rear view images** of vehicles.

![App Screenshot](app_screenshot.jpg)

---

# 🧠 Model Details

## Deep Learning Model

- **Architecture:** ResNet50
- **Technique:** Transfer Learning
- **Framework:** PyTorch
- **Training Images:** Around 1700 images
- **Number of Classes:** 6

## Damage Categories

The model predicts the following classes:

1. Front Normal
2. Front Crushed
3. Front Breakage
4. Rear Normal
5. Rear Crushed
6. Rear Breakage

## Model Performance

- Validation Accuracy: Approximately **80%**

---

# 🚀 Features

- Drag and drop vehicle image upload
- Automatic damage classification
- Deep learning based prediction
- Streamlit web interface
- Fast inference using ResNet50

---

# 📂 Project Structure
