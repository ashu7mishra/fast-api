from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        
    return data

@app.get("/")
def hello():
    return {"message: ": "Patient management system API."}

@app.get("/about")
def about():
    return {"message: ": "A fully functional API to manage  your patient records."}

@app.get("/view")
def view():
    return load_data()

@app.get("/patient/{patient_id}/")
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    # return {"message:": "Patient not found"}
    raise HTTPException(status_code=404, detail='patient_not_found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or BMI'), order: str = Query('asc', description='Sort in asc or desc order')):
    
    valid_fields = ['height', 'weight', 'BMI']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid field. Select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid field. Select from ['asc', 'desc']")
    
    data = load_data()
    sort_order = order=='desc'

    return sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    