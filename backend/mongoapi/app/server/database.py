from pymongo import MongoClient
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")
client = MongoClient(MONGO_DETAILS)

# Define your database and collections here
database = client.users
collection = database.users_collection

def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"]
    }

async def retrieve_all_items():
    items = []
    cursor = collection.find()
    for item in cursor:
        items.append(item_helper(item))
    return items

async def retrieve_item(item_id: str):
    cursor = collection.find_one({"_id": ObjectId(item_id)})
    return [item_helper(cursor)]

async def update_item_in_db(item_id: str, updated_item: dict) -> bool:
    cursor = collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item})
    return cursor.modified_count > 0

async def delete_item_from_db(item_id: str) -> bool:
    cursor = collection.delete_one({"_id": ObjectId(item_id)})
    return cursor.deleted_count > 0