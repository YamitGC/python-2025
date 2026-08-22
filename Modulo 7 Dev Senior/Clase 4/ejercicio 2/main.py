from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.middleware("http")
async def catch_all_exceptions(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"detalle": "Internal server error"}
        )
        
@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/error")
async def generate_error():
    #raise ValueError("Esti es un error intencional")
    raise HTTPException(status_code=400, detail="This is a intentional error")