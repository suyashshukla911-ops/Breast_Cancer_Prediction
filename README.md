AI-Assisted Breast Cancer Risk Screening Tool

An AI-driven health-tech prototype developed for Codecure, a flagship event of SPIRIT 2026 – IIT (BHU) Varanasi.
This project leverages machine learning to provide early risk screening support for breast cancer using diagnostic features derived from Fine Needle Aspiration (FNA) imaging.

⚠️ Disclaimer: This tool is intended for screening and decision support only.
It is NOT a medical diagnosis system and must not replace professional clinical judgment.

📌 Problem Statement

Breast cancer is one of the leading causes of cancer-related mortality among women worldwide.
Although early detection significantly improves survival rates, access to expert screening tools and awareness remains limited, especially in resource-constrained settings.

There is a need for a scalable, AI-assisted screening solution that can:

Analyze diagnostic features efficiently

Provide early risk indication

Support clinicians and patients in decision-making

💡 Proposed Solution

This project presents a web-based AI screening system that:

Accepts 30 standardized diagnostic features

Applies K-Nearest Neighbors (KNN) and Artificial Neural Networks (ANN)

Outputs:

Risk classification (Benign / Malignant)

ANN probability score

Risk level (Low / High)

Provides transparent and ethical AI-based screening feedback

🧠 Machine Learning Models Used
🔹 K-Nearest Neighbors (KNN)

Used as a baseline classifier

Helps compare traditional ML with deep learning

Number of neighbors: k = 5

🔹 Artificial Neural Network (ANN)

Two hidden layers with 16 neurons each

Activation: ReLU (hidden layers), Sigmoid (output)

Optimizer: Adam

Loss function: Binary Cross-Entropy

Demonstrates superior performance on complex, non-linear medical data

📊 Experimental results show that ANN achieves higher accuracy and ROC-AUC compared to KNN for this dataset.

🏗️ System Architecture
Frontend (HTML / CSS / JS)
        ↓
Flask REST API (Backend)
        ↓
Feature Scaling (StandardScaler)
        ↓
ML Models (KNN + ANN)
        ↓
Risk Prediction + Probability Output

🛠️ TechStack
Frontend
HTML
CSS
JavaScript (Fetch API)
Backend
Python
Flask
Flask-CORS
Machine Learning
Scikit-learn
TensorFlow / Keras
NumPy
Joblib
📁 Project Structure
codecure_breast_cancer_ai/
│
├── backend/
│   ├── app.py
│   ├── knn_model.pkl
│   ├── scaler.pkl
│   ├── ann_model.h5
│   └── requirements.txt
│
├── model/
│   ├── train_knn.py
│   └── train_ann.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md

🚀 How to Run the Project
1️⃣ Install Dependencies
pip install -r backend/requirements.txt
2️⃣ Train and Save Models
python model/train_knn.py
python model/train_ann.py
3️⃣ Start Backend Server
cd backend
python app.py
Backend will run at:
http://127.0.0.1:5000
4️⃣ Launch Frontend
Open:
frontend/index.html
in a web browser.
🧪 Sample Test Inputs
🟢 Benign Case (Low Risk)
12.45,15.7,82.6,477.1,0.089,0.078,0.045,0.029,0.165,0.058,
0.35,1.02,2.4,26.5,0.006,
0.015,0.018,0.009,0.016,0.002,
13.8,18.2,90.1,600.3,0.11,
0.17,0.19,0.075,0.22,0.07
🔴 Malignant Case (High Risk)
19.3,25.4,130.0,1200.0,0.11,0.25,0.30,0.16,0.22,0.075,
1.2,2.5,8.0,120.0,0.012,
0.05,0.08,0.04,0.04,0.01,
22.5,30.1,150.0,1800.0,0.16,
0.45,0.55,0.30,0.45,0.12
⚖️ Ethical Considerations
No personal or patient-identifiable data is stored
Dataset used is public, anonymized, and widely accepted
The system is not a diagnostic substitute
Designed strictly for awareness and decision support
🔮 Future Scope
Integration with medical imaging pipelines
Model explainability (SHAP / LIME)
Mobile application support
Secure cloud deployment
Clinical validation with real-world data
🏁 Conclusion
This project demonstrates how AI-driven models can assist in early cancer risk screening, enhance health literacy, and support clinical decision-making while maintaining ethical and professional standards.
