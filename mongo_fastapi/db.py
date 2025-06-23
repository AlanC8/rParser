from motor.motor_asyncio import AsyncIOMotorClient
from functools import lru_cache

class Settings:
    mongo_uri: str = "mongodb://localhost:27017"
    db_name: str = "parser"

@lru_cache()
def get_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(Settings().mongo_uri)

def get_db():
    return get_client()[Settings().db_name]
