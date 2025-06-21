from random import choice, randint
from datetime import datetime, timedelta
from uuid import uuid4
from pydantic import BaseModel
from faker import Faker

fake = Faker('en_IE')

department_doctors={
    "Cardiology": ["Dr. O'Connor", "Dr. Byrne"],
    "Neurology":["Dr. Walsh", "Dr. Kavanagh"],
    "Oncology": ["Dr. Murphy", "Dr. Doyle"],
    "Orthopedics": ["Dr. Brennan", "Dr. Nolan"],
    "Emergency": ["Dr. Ryan", "Dr. Gallagher"],
    "Pediatrics": ["Dr. Kelly", "Dr. Duffy"]
}

status_options = ["Admitted", "Discharged", "In Treatment", "Critical"]
appointment_statuses = ["Scheduled", "Completed", "No-Show", "Cancelled"]


admission_reasons = {
    "Cardiology": ["Chest pain", "Irregular heartbeat", "Heart attack"],
    "Neurology": ["Seizures", "Stroke", "Headache"],
    "Oncology": ["Chemotherapy", "Tumor diagnosis"],
    "Orthopedics": ["Fracture", "Knee replacement", "Back pain"],
    "Emergency": ["Accident", "Unconscious", "Severe bleeding"],
    "Pediatrics": ["Fever", "Flu", "Allergy"]
}

class Patient(BaseModel):
    patient_id: str
    name: str
    age: int
    gender: str
    admission_reason: str
    admitted_at: datetime
    department: str
    assigned_doctor: str
    status: str

class Appointment(BaseModel):
    appointment_id: str
    patient_id: str
    scheduled_for: datetime
    doctor: str
    department: str
    status: str


def generate_patient():
    department = choice(list(department_doctors.keys()))
    doctor = choice(department_doctors[department])
    reason = choice(admission_reasons[department])

    # Age logic (you can adjust these ranges by department)
    if department == "Pediatrics":
        age = randint(1, 15)
    elif department == "Cardiology":
        age = randint(45, 90)
    else:
        age = randint(16, 80)
        
    return Patient(
        patient_id=f"P_{uuid4().hex[:8].upper()}",
        name=fake.name(),
        age=age,
        gender=choice(["Male", "Female", "Other"]),
        admission_reason=reason,
        admitted_at=datetime.utcnow(),
        department=department,
        assigned_doctor=doctor,
        status=choice(status_options)
    )

def generate_appointment(patient_id: str, department: str, doctor: str):
    scheduled_days_ahead = choice(range(-10, 10))  # past or future
    scheduled_time = datetime.utcnow() + timedelta(days=scheduled_days_ahead, hours=choice(range(9, 17)))

    return Appointment(
        appointment_id=f"A_{uuid4().hex[:8].upper()}",
        patient_id=patient_id,
        scheduled_for=scheduled_time,
        doctor=doctor,
        department=department,
        status=choice(appointment_statuses)
    )