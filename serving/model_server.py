from fastapi import FastAPI
import mlflow
import pickle

app = FastAPI()
model = mlflow.pyfunc.load_model('models:/production/Production')

@app.post('/predict')
def predict(data: dict):
    features = [data['feature1'], data['feature2'], data['feature3']]
    prediction = model.predict([features])
    return {'prediction': prediction.tolist()[0]}
