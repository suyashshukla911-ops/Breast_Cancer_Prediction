from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import tensorflow as tf

app = Flask(__name__)
CORS(app)  


# Load models
knn = joblib.load("knn_model.pkl")
scaler = joblib.load("scaler.pkl")
ann = tf.keras.models.load_model("ann_model.h5")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    features = np.array(data).reshape(1, -1)
    features_scaled = scaler.transform(features)
    if len(data) != 30:
     return jsonify({
        "error": "Exactly 30 feature values are required."
    }), 400


    knn_pred = knn.predict(features_scaled)[0]
    ann_prob = ann.predict(features_scaled)[0][0]

    result = {
        "KNN_Prediction": "Benign" if knn_pred == 1 else "Malignant",
        "ANN_Probability": round(float(ann_prob), 3),
        "ANN_Prediction": "Benign" if ann_prob >= 0.5 else "Malignant",
        "Risk_Level": "High" if ann_prob < 0.5 else "Low",
        "Disclaimer": "This is an AI-assisted screening tool, not a medical diagnosis."
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
