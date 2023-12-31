from pymongo import MongoClient
from bson.objectid import ObjectId
from decouple import config

MONGO_URI = config("MONGO_URI")
client = MongoClient(MONGO_URI)

# Define your database and collections here
database = client.users
collection = database.users_collection

def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "Title": item["Title"],
        "Objective": item["Objective"],
        "Materials": item["Materials"],
        "Procedure": item["Procedure"],
        "Assessment": item["Assessment"]
    }

def ret_link(item) -> dict:
    return {
        "Title": item["Title"],
        "Objective": item["Objective"],
        "Materials": item["Materials"],
        "Procedure": item["Procedure"],
        "Assessment": item["Assessment"]
    }

async def retrieve_all_items():
    items = []
    cursor = collection.find()
    for item in cursor:
        items.append(item_helper(item))
    return items

async def retrieve_item(item_id: str):
    cursor = collection.find_one({"_id": ObjectId(item_id)})
    return [ret_link(cursor)]

async def retrieve_links(session_id: str):
    cursor = collection.find({"SessionId": session_id})
    links = []
    for item in cursor:
        links.append(str(item["_id"]))
    return links

async def update_item_in_db(item_id: str, updated_item: dict) -> bool:
    cursor = collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item})
    return cursor.modified_count > 0

async def delete_item_from_db(item_id: str) -> bool:
    cursor = collection.delete_one({"_id": ObjectId(item_id)})
    return cursor.deleted_count > 0