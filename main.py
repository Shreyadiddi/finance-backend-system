from fastapi import FastAPI
from database.connection import engine, Base
from routes.transaction_routes import router as transaction_router
from routes.analytics_routes import router as analytics_router
from models import user
from routes.user_routes import router as user_router

app = FastAPI()

#Create tables
Base.metadata.create_all(bind=engine)

app.include_router(transaction_router)

@app.get("/")
def home():
    return {"message": "Finance Backend is Running"}

app.include_router(analytics_router)

app.include_router(user_router)