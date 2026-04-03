# Finance Backend System

A scalable backend system for managing and analyzing financial transactions, built using **FastAPI**.


## Features

### 🔹 Financial Management
- Create, read, update, delete transactions
- Filter by type, category, and date range

### 🔹 Analytics
- Total income & expenses
- Current balance
- Category-wise breakdown

### 🔹 User & Role Management
- Roles: Admin, Analyst, Viewer
- Role-based access control

### 🔹 Architecture
- Modular structure:
  - Routes
  - Services
  - Models
  - Schemas
  - Utilities


## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic



##  Project Structure
finance-backend-system/
│
├── main.py
├── database/
├── models/
├── schemas/
├── routes/
├── services/
├── utils/


---

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/finance-backend-system.git
cd finance-backend-system
```
### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install Dependencies
pip install fastapi uvicorn sqlalchemy pydantic email-validator

### 4. Run Server
uvicorn main:app --reload

### 5. Open API Documents
http://127.0.0.1:8000/docs

### 6. Role-Based Access

| Role    | Permissions      |
| ------- | ---------------- |
| Admin   | Full access      |
| Analyst | View + analytics |
| Viewer  | View only        |

### 7. Example APIs
- POST /transactions
- GET /transactions
- PUT /transactions/{id}
- DELETE /transactions/{id}
- GET /analytics/summary
- POST /users

### 8.Key Highlights
- Clean backend architecture
- Role-based authorization
- Real-world financial analytics
- Scalable and maintainable code structure

### Author -
*Shreya*


