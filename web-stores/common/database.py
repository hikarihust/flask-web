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
    