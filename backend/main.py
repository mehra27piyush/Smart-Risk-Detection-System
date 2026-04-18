from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import predict_risk

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Smart Risk Detection API Running"}

@app.get("/predict")
def risk(age: int, hr: int, ox: int):
    result = predict_risk(age, hr, ox)
    return {"risk": result}