from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Medicine
import schemas
import crud
from routers import meds, reminders
from scheduler import scheduler  # ✅ use the scheduler from the external file

# Create DB tables
Base.metadata.create_all(bind=engine)

# Dummy ping job already handled in scheduler.py

# Dummy data insert (only once)
def populate_dummy_meds():
    db: Session = SessionLocal()
    existing = db.query(Medicine).all()
    existing_set = {(m.name.lower(), m.pharmacy.lower()) for m in existing}

    sample_data = [
        {"name": "Dolo 650", "pharmacy": "HealthPlus Med Store", "location": "Tech Market"},
        {"name": "Paracetamol", "pharmacy": "ABC Meds", "location": "Main Gate Market"},
        {"name": "Cetrizine", "pharmacy": "Wellness Forever", "location": "RP Hall Road"},
        {"name": "Azithromycin 500", "pharmacy": "Apollo Pharmacy", "location": "Tikka, Hostel Zone"},
        {"name": "Metformin 500", "pharmacy": "Medico Point", "location": "Nalanda Market"},
        {"name": "Ibuprofen", "pharmacy": "IIT Medical Corner", "location": "Technology Students Gymkhana"},
        {"name": "Amoxicillin", "pharmacy": "MediCare Plus", "location": "KR Market"},
        {"name": "Pantoprazole", "pharmacy": "Sunrise Pharmacy", "location": "LBS Hall Area"},
        {"name": "Losartan", "pharmacy": "Green Cross Meds", "location": "SR Hall Street"},
        {"name": "Atorvastatin", "pharmacy": "CarePoint Meds", "location": "RP Market"},
        {"name": "Allegra", "pharmacy": "Apollo Pharmacy", "location": "Tikka"},
        {"name": "Montelukast", "pharmacy": "HealthHub Pharmacy", "location": "LBS Market"},
        {"name": "Aspirin", "pharmacy": "Shree Medico", "location": "Main Market"},
        {"name": "Benedryl", "pharmacy": "New Care Pharmacy", "location": "Tech Market"},
        {"name": "Levocetirizine", "pharmacy": "ReliefMed", "location": "RP Hall Lane"},
        {"name": "Domperidone", "pharmacy": "MediStore", "location": "Nalanda Lane"},
        {"name": "Ranitidine", "pharmacy": "KGP Medico", "location": "LBS Hall"},
        {"name": "Omeprazole", "pharmacy": "Medical World", "location": "SR Hostel Market"},
        {"name": "Cetirizine", "pharmacy": "Lifeline Pharmacy", "location": "Tech Market"},
        {"name": "Dicyclomine", "pharmacy": "Apollo Pharmacy", "location": "KR Market"},
        {"name": "Hydroxychloroquine", "pharmacy": "MediHelp", "location": "RP Market"},
        {"name": "Zincovit", "pharmacy": "Health Aid", "location": "Tikka Street"},
        {"name": "Neurobion Forte", "pharmacy": "BetterLife Meds", "location": "Tech Market"},
        {"name": "Calpol", "pharmacy": "Swasthya Pharmacy", "location": "SR Hall Area"},
        {"name": "Crocin", "pharmacy": "IIT Medico", "location": "Gymkhana Area"},
        {"name": "ORS Sachet", "pharmacy": "Medical Relief", "location": "Main Gate"},
        {"name": "Loperamide", "pharmacy": "KR MedStore", "location": "Nalanda Gate"},
        {"name": "Chlorpheniramine", "pharmacy": "Apollo Pharmacy", "location": "Tikka"},
        {"name": "Naproxen", "pharmacy": "QuickMeds", "location": "Tech Market"},
        {"name": "Aceclofenac", "pharmacy": "Good Health Pharmacy", "location": "Main Market"},
    ]

    added = 0
    for item in sample_data:
        key = (item["name"].lower(), item["pharmacy"].lower())
        if key not in existing_set:
            crud.create_medicine(db, schemas.MedicineCreate(**item))
            added += 1

    db.close()
    print(f"✅ Added {added} new medicines.")

# FastAPI app init
app = FastAPI(title="MedMate API")

# CORS config for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update if deploying
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dummy medicine data
populate_dummy_meds()

# Register routers
app.include_router(meds.router)
app.include_router(reminders.router)
