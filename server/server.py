from fastapi import FastAPI
import utils

app = FastAPI()

utils.load_artifacts()


@app.get('/get_categories')
def get_categories():
    return utils.__categories


@app.post('/predict')
def predict(request:utils.InputSchema):
    return utils.predict(request)