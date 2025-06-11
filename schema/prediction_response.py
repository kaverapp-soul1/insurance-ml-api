from math import e
from pydantic import BaseModel,Field
from typing import List, Optional,Dict


class PredictionResponse(BaseModel):
    predicted_category:str=Field(
        ..., 
        description="The predicted category of the input text",
        example="High"
        )
    confidence_score:float=Field(
        ..., 
        description="The confidence score of the prediction, ranging from 0 to 1",
        example=0.95

        )
    class_probabilities:Dict[str,float]=Field(
        ...,
        description="A dictionary containing the probabilities of each class",
        example={
            "High": 0.95,
            "Medium": 0.03,
            "Low": 0.02
        }
    )
    