from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controllers import auth_controller, post_controller
from .database import engine
from .models import base

base.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MVC Blog API",
    description="A blog API built with FastAPI following MVC pattern",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_controller.router)
app.include_router(post_controller.router)

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the MVC Blog API"} 