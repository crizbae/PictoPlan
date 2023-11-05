from fastapi import FastAPI
from .routes.item_routes import router as item_routes

app = FastAPI()

# Include the router defined in routes.py
app.include_router(item_routes, tags=["User"], prefix="/user")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}