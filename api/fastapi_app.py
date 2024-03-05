from fastapi import FastAPI
import pandas as pd
import pickle
from pydantic import BaseModel


class MlRequest(BaseModel):
    model: str
    t: float
    h: float
    co2: float
    mox1: float
    mox2: float
    cov: float
    hour: float


app = FastAPI()


def predict(model, t, h, co2, mox1, mox2, cov, hour):
    prediction = model.predict(pd.DataFrame({'temperature': [t], 'humidity': [h], 'CO2MG811Value': [co2],
                                             'MOX1': [mox1], 'MOX2': [mox2], 'COValue': [cov], 'hour': [hour]}))[0]
    print('result = ', prediction)
    return int(prediction)


@app.post("/model-predict")
async def ml_predict(parameters: MlRequest):
    if parameters.model == 'LogReg':
        using_model = pickle.load(open('models/log_reg_model.pkl', 'rb'))
    elif parameters.model == 'SVM':
        using_model = pickle.load(open('models/svm_model.pkl', 'rb'))
    else:
        return -1
    return predict(using_model, parameters.t, parameters.h, parameters.co2, parameters.mox1,
                   parameters.mox2, parameters.cov, parameters.hour)
