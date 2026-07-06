from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import rag
from database import Base, engine

from models import company as company_model
from models import job as job_model
from models import users as user_model

from routers import auth
from routers import company
from routers import job
from routers import chat

app = FastAPI(title="TalentSpark API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth.router)
app.include_router(company.router)
app.include_router(job.router)
app.include_router(chat.router)
app.include_router(rag.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to TalentSpark API"}


@app.get("/about")
def about():
    return {"about": "TalentSpark Backend API"}


@app.get("/contact")
def contact():
    return {"contact": "Contact Page"}