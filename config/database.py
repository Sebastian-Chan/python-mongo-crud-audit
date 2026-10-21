import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "inventario_audit_db")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def init_db():
    db.usuarios.create_index("email", unique=True)

def get_database():
    return db