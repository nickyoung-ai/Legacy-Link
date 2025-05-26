from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": " Legacy Link backend ready to launch"}