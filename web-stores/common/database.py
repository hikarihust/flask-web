import os
from typing import Dict
import pymongo


class Database:
    URI = "mongodb://127.0.0.1:27017/pricing"
    DATABASE = pymongo.MongoClient(URI).get_default_database()

    @classmethod
    def insert(cls, collection: str, data: Dict) -> None:
        cls.DATABASE[collection].insert(data)

    @classmethod
    def find(cls, collection: str, query: Dict) -> pymongo.cursor:
        return cls.DATABASE[collection].find(query)

    @classmethod
    def find_one(cls, collection: str, query: Dict) -> Dict:
        return cls.DATABASE[collection].find_one(query)
    
    @classmethod
    def update(cls, collection: str, query: Dict, data: Dict) -> None:
        cls.DATABASE[collection].update(query, data, upsert=True)
    
    @classmethod
    def remove(cls, collection: str, query: Dict) -> Dict:
        return cls.DATABASE[collection].remove(query)
    