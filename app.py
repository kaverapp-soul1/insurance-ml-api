from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInputData
from model.predict import predict_output, MODEL_version

from schema.prediction_response import PredictionResponse

app=FastAPI()



@app.get("/")
async def read_root():
    return {"message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}

@app.get("/health")
async def health_check():
    return {
        "status": "OK",
        "version": MODEL_version,
        "message": "API is running smoothly.",
        "model_loaded": True,
        }

@app.post("/predict",response_model=PredictionResponse)
async def predict_premium(data:UserInputData):
    user_input={
        
                "bmi":data.bmi,
                "income_lpa":data.income,
                "age_group":data.age_group,
                "occupation":data.occupation,
                "city_tier":data.city_tier,
                "smoker_risk":data.smoker_risk,
                "bmi_risk_score":data.bmi_risk_score,
                "bmimeasure":data.bmimeasure
            
    }
    try:
        prediction= predict_output(user_input)
        if prediction is None:
            return JSONResponse(content={"error": "Prediction failed. Please check your input data."}, status_code=400)
    
        return JSONResponse(content={"predicted_category":prediction},status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)