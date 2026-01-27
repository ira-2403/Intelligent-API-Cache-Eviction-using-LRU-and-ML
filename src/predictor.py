import joblib
import numpy as np

model = joblib.load("models/reuse_predictor.pkl")

def predict_reuse(frequency, hit_ratio):
    features = np.array([[frequency, hit_ratio]])
    prediction = model.predict(features)
    return prediction[0]  # 1 = likely reuse, 0 = evict
