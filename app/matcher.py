def calculate_match_score(pet1_prefs: dict, pet2_prefs: dict) -> int:
    """Calcula score entre dos conjuntos de preferencias"""
    if not pet1_prefs or not pet2_prefs:
        return 0

    matches = sum(1 for k in pet1_prefs if k in pet2_prefs and pet1_prefs[k] == pet2_prefs[k])
    total = max(len(pet1_prefs), len(pet2_prefs))
    return int((matches / total) * 100)
