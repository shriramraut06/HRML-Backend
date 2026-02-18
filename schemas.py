from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date

class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

class EmployeeOut(BaseModel):
    id: int
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

    model_config = ConfigDict(from_attributes=True)

class AttendanceCreate(BaseModel):
    employee_id: int
    date: date
    status: str
