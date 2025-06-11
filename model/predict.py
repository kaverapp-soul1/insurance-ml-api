import pickle
import pandas as pd


with open("./model/insurance_model.pkl","rb") as f:
    model = pickle.load(f)

MODEL_version = "1.0.0"

class_labels=model.classes_.tolist()


def predict_output(user_input:dict):
    df = pd.DataFrame([user_input])
    prediction = model.predict(df)[0]
    probabilities=model.predict_proba(df)[0]
    confidence=max(probabilities)
    class_probs=dict(zip(class_labels,map(lambda p: round(p, 4), probabilities)))
    prediction = {
        "predicted_category": prediction,
        "confidence": round(confidence,4),
        "class_labels": class_probs
    }
    return prediction
