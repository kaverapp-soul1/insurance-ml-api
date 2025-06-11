from pydantic import BaseModel, Field, field_validator, computed_field
from typing import Literal, Annotated
from config.city_tier import tier1_cities, tier2_cities, tier3_cities




class UserInputData(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description="age required")]
    weight:Annotated[float,Field(...,gt=0,description="weight required")]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description="height required")]
    income:Annotated[float,Field(...,description="income required")]
    smoker:Annotated[bool,Field(...,description="smoker required")]
    city:Annotated[str,Field(...,description="city required")]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'],Field(...,description="occupation required")]

    @field_validator("city")
    def validate_city(cls, v: str) -> str:
        
        if not v:
            raise ValueError("City cannot be empty")
        return v.strip().title()
    


    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def bmimeasure(self)->str:
        bmi_value = self.bmi
        if bmi_value < 18.5:
            return "Underweight"
        elif 18.5 <= bmi_value < 25:
            return "Normal"
        elif 25 <= bmi_value < 30:
            return "Overweight"
        else:
            return "Obese"
    
    @computed_field
    @property
    def age_group(self)->str:
        age_val=self.age
        if age_val < 12:
            return "Child"
        elif 12 <= age_val < 19:
            return "Teen"
        elif 19 <= age_val < 59:
            return "Adult"
        else:
            return "Senior"
    
    @computed_field
    @property
    def bmi_risk_score(self)->str:
        if self.bmimeasure == "Underweight":
            return 1
        elif self.bmimeasure == "Normal":
            return 2
        elif self.bmimeasure == "Overweight":
            return 3
        else:
            return 4
        
    @computed_field
    @property
    def city_tier(self)->str:
        if self.city in tier1_cities:
            return 1
        elif self.city in tier2_cities:
            return 2
        elif self.city in tier3_cities:
            return 3
        else:
            return 0       
        
    @computed_field
    @property
    def smoker_risk(self)->str:
        if self.smoker:
            if self.bmimeasure=="Obese" and self.age_group=="Senior":
                return 'Very High' 
            elif self.bmimeasure in ['Underweight', 'Overweight']:
                return 'High'
            elif self.bmimeasure == 'Underweight':
                return 'High'
            else:
                return 'Medium'
        else:
            if self.bmimeasure == 'Obese' and self.age_group == 'Senior':
                return 'High'
            elif self.bmimeasure in ['Underweight', 'Overweight']:
                return 'Medium'
            else:
                return 'Low'
