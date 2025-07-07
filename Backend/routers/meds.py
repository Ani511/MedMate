from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import MedicineCreate, MedicineOut
from crud import create_medicine, get_medicines_by_name
from database import SessionLocal

router = APIRouter(prefix="/medicines", tags=["medicines"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MedicineOut)
def add_medicine(med: MedicineCreate, db: Session = Depends(get_db)):
    return create_medicine(db, med)

@router.get("/", response_model=list[MedicineOut])
def search_medicine(name: str, db: Session = Depends(get_db)):
    return get_medicines_by_name(db, name)
