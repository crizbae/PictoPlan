from fastapi import APIRouter, Depends, HTTPException
from ..database import collection
from ..models.item import Item
from ..database import retrieve_all_items, retrieve_item, update_item_in_db, delete_item_from_db                              

router = APIRouter()

@router.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    inserted_item = collection.insert_one(item_dict)
    item_id = str(inserted_item.inserted_id)
    del item_dict["_id"]
    item_dict["id"] = item_id
    return item_dict

@router.get("/items/")
async def get_all_items():
    items = await retrieve_all_items()
    return items

@router.get("/items/{item_id}")
async def get_item_by_id(item_id: str):
    item = await retrieve_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}")
async def update_item(item_id: str, updated_item: Item):
    updated_item = updated_item.dict()
    success = await update_item_in_db(item_id, updated_item)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {**updated_item, "id": item_id}

@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    success = await delete_item_from_db(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Item with ID {item_id} deleted successfully"}