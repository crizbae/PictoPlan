from fastapi import FastAPI
from routes import router as process_router

app = FastAPI()

# Include the router defined in routes.py
app.include_router(process_router, tags=["Processor"], prefix="/processor")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}