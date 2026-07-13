# 🚗 Vehicle Damage Detection App

An AI-powered **Vehicle Damage Detection Application** that identifies the type of damage present in a vehicle image using Deep Learning.

The application provides a simple drag-and-drop interface where users can upload a car image, and the model predicts the damage category.

The model is trained on **third-quarter front and rear view vehicle images**, therefore images should capture the **front or rear three-quarter view of the vehicle** for better prediction accuracy.

![App Screenshot](app_screenshot.jpg)


# 🧠 Model Details

## Deep Learning Approach

- **Model Architecture:** ResNet50
- **Technique:** Transfer Learning
- **Framework:** PyTorch
- **Training Dataset:** Around 1700 vehicle images
- **Number of Classes:** 6
- **Validation Accuracy:** Approximately 80%


## Damage Categories

The model classifies vehicle images into the following categories:

1. Front Normal
2. Front Crushed
3. Front Breakage
4. Rear Normal
5. Rear Crushed
6. Rear Breakage


# 🚀 Features

- Drag and drop vehicle image upload
- Automatic vehicle damage classification
- Deep learning-based prediction
- Fast inference using ResNet50
- Streamlit web interface
- Supports multiple damage categories


# 📂 Project Structure

```
Car-damage-prediction
│
├── app.py                         # Streamlit application
├── model_helper.py                # Model loading and prediction
├── requirements.txt               # Required dependencies
├── runtime.txt                    # Python version configuration
├── README.md
├── app_screenshot.jpg             # Application screenshot
│
├── model
│   └── saved_model.pth            # Trained ResNet50 model
│
├── dataset                        # Dataset directory
│
├── damage_prediction.ipynb        # Model training notebook
└── hyperparameter_tunning.ipynb   # Hyperparameter tuning notebook
```


# ⚙️ Installation and Setup

## 1. Clone Repository

```bash
git clone https://github.com/Abhi-19-05/Car-damage-prediction.git
```

Navigate to the project folder:

```bash
cd Car-damage-prediction
```


## 2. Install Dependencies

Install all required Python libraries:

```bash
pip install -r requirements.txt
```


## 3. Run Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.


# 🔄 Working Pipeline

```
Vehicle Image Upload
          |
          ↓
Image Preprocessing
          |
          ↓
ResNet50 Feature Extraction
          |
          ↓
Classification Layer
          |
          ↓
Damage Category Prediction
```


# 🛠️ Technologies Used

- Python
- PyTorch
- Torchvision
- ResNet50
- Streamlit
- Pillow
- NumPy
- OpenCV
- Scikit-learn


# 📊 Dataset Classes

| Class | Description |
|------|-------------|
| Front Normal | Vehicle front without damage |
| Front Crushed | Severe crushing damage on front side |
| Front Breakage | Broken components on front side |
| Rear Normal | Vehicle rear without damage |
| Rear Crushed | Severe crushing damage on rear side |
| Rear Breakage | Broken components on rear side |


# 📈 Model Training

The model was trained using transfer learning:

- Pre-trained ResNet50 backbone
- Frozen initial layers
- Fine-tuned deeper layers
- Custom fully connected classification layer
- Six-class damage classification


# 🌐 Deployment

The application can be deployed using:

- Streamlit Cloud
- AWS
- Docker
- Local machine


# 🔮 Future Improvements

- Increase dataset size
- Improve prediction accuracy
- Add damage severity estimation
- Estimate repair cost
- Add real-time camera detection
- Deploy as a mobile application


# 👨‍💻 Author

**Abhinandan Pakhare**

GitHub:
https://github.com/Abhi-19-05


⭐ If you find this project useful, consider giving it a star!
