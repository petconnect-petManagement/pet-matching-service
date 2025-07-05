from fastapi import APIRouter, HTTPException
from app.db import pet_profile_collection, pet_preferences_collection
from app.matcher import calculate_match_score

router = APIRouter(prefix="/api/v1/pet-matching", tags=["pet-matching"])

@router.get("/{pet_id}")
def match_pets(pet_id: str):
    pet = pet_profile_collection.find_one({"_id": pet_id})
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    prefs = pet_preferences_collection.find_one({"pet_id": pet_id})
    all_pets = pet_profile_collection.find({"_id": {"$ne": pet_id}})
    
    matches = []
    for other in all_pets:
        other_prefs = pet_preferences_collection.find_one({"pet_id": other["_id"]})
        score = calculate_match_score(prefs["preferences"] if prefs else {}, other_prefs["preferences"] if other_prefs else {})
        if score >= 50:
            matches.append({
                "pet_id": other["_id"],
                "score": score
            })

    return {"matches": sorted(matches, key=lambda x: -x["score"])}
