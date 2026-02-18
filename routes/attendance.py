from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Attendance, Employee
from schemas import AttendanceCreate

router = APIRouter(prefix="/api/attendance", tags=["Attendance"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /api/attendance
@router.post("/")
def mark_attendance(payload: AttendanceCreate, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == payload.employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    record = Attendance(**payload.dict())
    db.add(record)
    db.commit()
    return {"message": "Attendance marked"}

# GET /api/attendance/{employee_id}
@router.get("/{employee_id}")
def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    return db.query(Attendance).filter(Attendance.employee_id == employee_id).all()

# GET /api/attendance  AND  /api/attendance/

@router.get("/")
def list_all_attendance(db: Session = Depends(get_db)):
    return db.query(Attendance).all()
