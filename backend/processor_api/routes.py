from fastapi import APIRouter, Depends, HTTPException    
from processor import processor                      

router = APIRouter()

@router.post("/process/")
async def create_item(b64array: dict):
    if len(b64array) == 0:
        raise HTTPException(status_code=400, detail="Invalid request")
    lessons = processor(b64array)
    if len(lessons) == 0:
        raise HTTPException(status_code=404, detail="GPT failed")
    
    # call to backend?
    return lessons