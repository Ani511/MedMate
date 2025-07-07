from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import ReminderCreate, ReminderOut
from crud import create_reminder, get_reminders_by_user
from database import SessionLocal
from datetime import datetime, timedelta
# reminders.py
from scheduler import scheduler  # ✅ safe now


router = APIRouter(prefix="/reminders", tags=["reminders"])

# Dependency: DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/", response_model=ReminderOut)
def add_reminder(reminder: ReminderCreate, db: Session = Depends(get_db)):
    db_rem = create_reminder(db, reminder)

    # Parse reminder time (HH:MM) and convert to next valid datetime
    reminder_time = datetime.strptime(reminder.time, "%H:%M").time()
    now = datetime.now()
    run_time = datetime.combine(now.date(), reminder_time)
    if run_time < now:
        run_time += timedelta(days=1)

    # Scheduler job: placeholder (console log or backend trigger)
    scheduler.add_job(
        lambda: print(f"[🔔 Reminder Triggered] Take {reminder.medicine_name}"),
        "date",
        run_date=run_time,
        id=f"reminder_{db_rem.id}",
        replace_existing=True,
    )

    return db_rem

# ✅ Fetch reminders by user_id
@router.get("/", response_model=list[ReminderOut])
def list_user_reminders(user_id: str, db: Session = Depends(get_db)):
    return get_reminders_by_user(db, user_id)
