# Import class Database
from database import Database

db = Database()

volume_data = {
    "volnr": 1,
    "name": "Volume 1",
    "year": 2024
}

volume_data = {
    "volnr": 2,
    "name": "Volume 2",
    "year": 2025
}

volume_id = db.save_volume(volume_data)