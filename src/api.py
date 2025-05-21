from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pickle
import os
from typing import List, Optional

app = FastAPI(title="Housing Price Prediction API")

# Load the model and preprocessors
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model
model_path = os.path.join(BASE_DIR, "models", "gradient_boosting_model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load scalers
scaler_X_path = os.path.join(BASE_DIR, "models", "scaler_X.pkl")
scaler_y_path = os.path.join(BASE_DIR, "models", "scaler_y.pkl")

with open(scaler_X_path, 'rb') as f:
    scaler_X = pickle.load(f)
with open(scaler_y_path, 'rb') as f:
    scaler_y = pickle.load(f)

# Load encoders
encoders = {}
categorical_cols = [
    'mainroad', 'guestroom', 'basement',
    'hotwaterheating', 'airconditioning', 'prefarea',
    'furnishingstatus'
]

for col in categorical_cols:
    encoder_path = os.path.join(BASE_DIR, "models", f"encoder_{col}.pkl")
    with open(encoder_path, 'rb') as f:
        encoders[col] = pickle.load(f)

class HousingInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    parking: int
    prefarea: str
    furnishingstatus: str

class HousingResponse(BaseModel):
    predicted_price: float

@app.post("/predict", response_model=HousingResponse)
async def predict_price(input_data: HousingInput):
    try:
        # Convert input to DataFrame
        input_dict = input_data.dict()
        df_input = pd.DataFrame([input_dict])
        
        # Encode categorical variables using saved encoders
        for col in categorical_cols:
            df_input[col] = encoders[col].transform(df_input[col])
        
        # Scale features
        X_scaled = scaler_X.transform(df_input)
        
        # Make prediction
        y_pred_scaled = model.predict(X_scaled)
        y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1))
        
        return {"predicted_price": float(y_pred[0][0])}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to Housing Price Prediction API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 