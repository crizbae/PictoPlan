from fastapi import APIRouter, Depends, HTTPException    
from processor import processor  
import requests        
import json      
import ast      

router = APIRouter()

@router.post("/process/")
async def create_item(b64array: dict):
    print("Part1!")
    if len(b64array) == 0:
        raise HTTPException(status_code=400, detail="Invalid request")
    uuid = list(b64array.keys())[0]
    uuid = uuid.split('-')[0]
    lessons = processor(b64array)
    print("Part2!")
    if len(lessons) == 0:
        raise HTTPException(status_code=404, detail="GPT failed")
    url = 'https://mongo.pictoplan.org/item' 
    print(lessons)
    lessons = [json.loads(lesson) for lesson in lessons]
    for lesson in lessons:
        lesson['SessionId'] = uuid
        response = requests.post(url, json=lesson)

    url = 'https://mongo.pictoplan.org/item/session/' + uuid
    response = requests.get(url).json()
    return response