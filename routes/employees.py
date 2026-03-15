from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Employee
from schemas import EmployeeCreate, EmployeeOut

router = APIRouter(prefix="/api/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=EmployeeOut)
@router.post("/", response_model=EmployeeOut)
def add_employee(payload: EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(Employee).filter(
        (Employee.employee_id == payload.employee_id) |
        (Employee.email == payload.email)
    ).first()

    if existing:
        raise HTTPException(status_code=409, detail="Employee ID or Email already exists")

    emp = Employee(**payload.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

@router.get("", response_model=list[EmployeeOut])
def list_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.delete("/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}
