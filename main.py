from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, profile
import models
from database import engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Example CORS setup (customize origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(profile.router)

@app.get("/")
def read_root():
    return {"message": "Legacy Link backend ready to launch"}


from .import auth_utils


