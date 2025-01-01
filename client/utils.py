import requests
import json


url = "http://fastapi:8080"

def button_availability(make,vehicle_class,cylinders,transmission,fuel_type,engine_size,fuel_consumption,gear):
    if None in [make,vehicle_class,cylinders,transmission,fuel_type,engine_size,fuel_consumption,gear]:
        return False
    else:
        return True

def get_categories():
    response = requests.get(f'{url}/get_categories')
    bytes_data = response.content
    categories = json.loads(bytes_data.decode('utf-8'))

    return categories

def get_prediction(make,vehicle_class,cylinders,transmission,fuel_type,engine_size,fuel_consumption,gear):
    input_data = {
        "make":str(make),
        "vehicle_class": str(vehicle_class),
        "cylinders": str(cylinders),
        "transmission": str(transmission),
        "fuel_type": str(fuel_type),
        "engine_size": float(engine_size),
        "fuel_consumption": float(fuel_consumption),
        "gear": int(gear)
    }
    json_data = json.dumps(input_data)
    response = requests.post(f'{url}/predict',data=json_data)
    bytes_data = response.content
    bytes_data = json.loads(bytes_data.decode('utf-8'))
    return round(bytes_data['data'],2)
