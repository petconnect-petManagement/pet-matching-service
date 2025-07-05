from pymongo import MongoClient
from app.config import MONGODB_URI, PET_PROFILE_DB, PREFERENCES_DB

client = MongoClient(MONGODB_URI)

pet_profile_collection = client[PET_PROFILE_DB]["pets"]
pet_preferences_collection = client[PREFERENCES_DB]["preferences"]
