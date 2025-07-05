# 🐾 Pet Matching Service

Microservicio para sugerir mascotas compatibles dentro de PetConnect.

## 🚀 Funcionalidad

- Calcula similitud entre mascotas basado en preferencias
- Devuelve matches con puntaje ≥ 50%

## 🧪 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/api/v1/pet-matching/:pet_id` | Obtener matches para una mascota |

## ⚙️ Tecnologías

- Python 3.11
- FastAPI
- MongoDB
- Docker

## 📦 Variables de entorno

- `PORT=3017`
- `MONGODB_URI=mongodb://mongo:27017`
- `PET_PROFILE_DB=petprofiledb`
- `PREFERENCES_DB=petpreferencesdb`
- `JWT_SECRET=supersecreto123diegopetconnect456`
