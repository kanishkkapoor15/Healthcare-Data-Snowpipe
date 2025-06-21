from typing import Dict
import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    account="",
    user="",
    password="",  
    role="",
    warehouse="",
    database="HOSPITAL_DATA",
    schema="RAW"
)

# Optional: test the connection
cursor = conn.cursor()
cursor.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE();")
print("✅ Connection successful. Current context:")
print(cursor.fetchone())
cursor.close()

#  Patient insert function 
def insert_patient(patient: Dict):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (
            patient_id, "name", age, gender, admission_reason,
            admitted_at, department, assigned_doctor, status
        ) VALUES (
            %(patient_id)s, %(name)s, %(age)s, %(gender)s, %(admission_reason)s,
            %(admitted_at)s, %(department)s, %(assigned_doctor)s, %(status)s
        );
    """, patient)
    cursor.close()

# Appointment insert function
def insert_appointment(appt: Dict):
    cursor = conn.cursor()
    cursor.execute(""" 
        INSERT INTO appointments (
            appointment_id, patient_id, scheduled_for,
            doctor, department, status
        ) VALUES (
            %(appointment_id)s, %(patient_id)s, %(scheduled_for)s,
            %(doctor)s, %(department)s, %(status)s
        );
    """, appt)
    cursor.close()