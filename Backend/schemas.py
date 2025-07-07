from pydantic import BaseModel

class MedicineCreate(BaseModel):
    name: str
    pharmacy: str
    location: str

class MedicineOut(MedicineCreate):
    id: int
    class Config:
        orm_mode = True

class ReminderCreate(BaseModel):
    user_id: str
    medicine_name: str
    time: str

class ReminderOut(ReminderCreate):
    id: int
    class Config:
        orm_mode = True
