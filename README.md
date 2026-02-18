# HRMS Lite - FastAPI Backend

## Run Locally
python -m venv venv
source venv/bin/activate  (Windows: venv\Scripts\activate)
pip install -r requirements.txt
uvicorn main:app --reload

## Endpoints (kept same as Flask)
GET    /api/employees
POST   /api/employees
DELETE /api/employees/{id}

POST   /api/attendance
GET    /api/attendance/{employee_id}
# Backend-HRMS-Lite