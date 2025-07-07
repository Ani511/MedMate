from sqlalchemy.orm import Session
from models import Medicine, Reminder
from schemas import MedicineCreate, ReminderCreate

# Medicine
def create_medicine(db: Session, medicine: MedicineCreate):
    db_med = Medicine(**medicine.dict())
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med

def get_medicines_by_name(db: Session, name: str):
    return db.query(Medicine).filter(Medicine.name.ilike(f"%{name}%")).all()

# Reminder
def create_reminder(db: Session, reminder: ReminderCreate):
    db_rem = Reminder(**reminder.dict())
    db.add(db_rem)
    db.commit()
    db.refresh(db_rem)
    return db_rem

def get_reminders_by_user(db: Session, user_id: str):
    return db.query(Reminder).filter(Reminder.user_id == user_id).all()
