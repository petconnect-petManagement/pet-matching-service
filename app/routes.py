from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.db import pet_profile_collection, pet_preferences_collection
from app.matcher import calculate_match_score

router = APIRouter(prefix="/api/v1/pet-matching", tags=["pet-matching"])

@router.get("/{pet_id}")
def match_pets(pet_id: str):
    print(f"[DEBUG] pet_id recibido: {pet_id}")

    try:
        pet_obj_id = ObjectId(pet_id)
        print(f"[DEBUG] Convertido a ObjectId: {pet_obj_id}")
    except Exception as e:
        print(f"[ERROR] pet_id inválido: {e}")
        raise HTTPException(status_code=400, detail="Invalid pet_id format")

    pet = pet_profile_collection.find_one({"_id": pet_obj_id})
    print(f"[DEBUG] Resultado de find_one para pet: {pet}")

    if not pet:
        print("[ERROR] Pet no encontrado en la base de datos.")
        raise HTTPException(status_code=404, detail="Pet not found")

    prefs = pet_preferences_collection.find_one({"pet_id": pet_id})
    print(f"[DEBUG] Preferencias encontradas: {prefs}")

    all_pets = pet_profile_collection.find({"_id": {"$ne": pet_obj_id}})
    matches = []

    for other in all_pets:
        other_id = str(other["_id"])
        other_prefs = pet_preferences_collection.find_one({"pet_id": other_id})
        score = calculate_match_score(
            prefs["preferences"] if prefs else {},
            other_prefs["preferences"] if other_prefs else {}
        )
        if score >= 50:
            matches.append({
                "pet_id": other_id,
                "score": score
            })

    print(f"[DEBUG] Matches calculados: {matches}")

    return {"matches": sorted(matches, key=lambda x: -x["score"])}
