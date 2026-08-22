from fastapi import FastAPI, HTTPException
import logging 

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def root():
    logging.info("Root endpoint called")
    return {"message": "Welcome to my new API"}

@app.get("/log")
def log_demo():
    logging.info("Log endpoint called")
    return {"message": "This is a log demo"}
