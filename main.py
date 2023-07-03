from fastapi import FastAPI, Depends
import uvicorn
from pydantic import BaseModel 
import joblib

app = FastAPI(title="API Startup",description="using FastAPI",version="1.0")


class Data (BaseModel):
    rd_spend : float = 73721.6156		
    administration : float = 121344.6396
    marketing_spend : float = 211025.0978

@app.on_event("startup")
def startup_event():
    "modello *.pkl di ML"
    global model 
    model = joblib.load("startup.pkl")
    print(" MODEL LOADED!!")
    return model


@app.get("/")
def hello():
    return {"--> http://127.0.0.1:8000/docs <--"}


#GET
@app.get("/predict")
async def predict_get(data:Data=Depends()):
    try:
        X = [[data.rd_spend, data.administration, data.marketing_spend]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return res
    except:
        return {"result":"error"}

#POST
@app.post("/predict")
async def predict_post(data:Data):
    try:
        X = [[data.rd_spend, data.administration, data.marketing_spend]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return res
        res.json()
    except:
        return {"result":"error"}


if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)