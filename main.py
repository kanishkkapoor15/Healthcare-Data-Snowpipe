from fastapi import FastAPI
from generator import generate_patient, generate_appointment
from snowflake_connector import insert_patient, insert_appointment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hospital Simulation API is running"}

@app.get("/generate-and-insert/patient-with-appointment")
def generate_patient_and_appointment(count: int = 100):
    inserted = []

    for _ in range(count):
        patient = generate_patient()
        insert_patient(patient.dict())

        appt = generate_appointment(patient.patient_id, patient.department, patient.assigned_doctor)
        insert_appointment(appt.dict())

        inserted.append({
            "patient": patient.dict(),
            "appointment": appt.dict()
        })

    return {
        "status": f"{count} patient-appointment pairs inserted successfully",
        "sample_records": inserted[:5]  # Return only first 5 for brevity
    }