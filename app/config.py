import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", 3017))
MONGODB_URI = os.getenv("MONGODB_URI")
PET_PROFILE_DB = os.getenv("PET_PROFILE_DB")
PREFERENCES_DB = os.getenv("PREFERENCES_DB")
JWT_SECRET = os.getenv("JWT_SECRET")
