import json
import numpy as np
import joblib
from pydantic import BaseModel

class InputSchema(BaseModel):
    make: str
    vehicle_class: str
    cylinders: str
    transmission: str
    fuel_type: str
    engine_size: float
    fuel_consumption: float
    gear: int


__input_columns = None
__categories = None
__model = None

def load_artifacts():
    with open('./artifacts/input_columns.json','r') as f:
        global __input_columns
        global __categories
        data = json.load(f)
        __input_columns = data['input_columns']
        __categories = data['categories']

    global __model
    __model = joblib.load('./artifacts/model.joblib')

def predict(request):
    
    inp = np.zeros([1,len(list(__input_columns))])

    inp[:,0] = request.engine_size
    inp[:,1] = request.fuel_consumption
    inp[:,2] = request.gear

    inp[:,__input_columns.index(request.make)] = 1
    inp[:,__input_columns.index(request.vehicle_class)] = 1
    inp[:,__input_columns.index(request.cylinders)] = 1
    inp[:,__input_columns.index(request.transmission)] = 1
    inp[:,__input_columns.index(request.fuel_type)] = 1


    return {"data":__model.predict(inp)[0]}
