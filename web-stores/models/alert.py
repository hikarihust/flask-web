from typing import List, Dict
import uuid
from common.database import Database
from models.item import Item
from models.model import Model


class Alert(Model):
    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self.collection = "alerts"
        self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item._id
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self) -> None:
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reached a price under {self.price_limit}. Latest price: {self.item.price}.")
    
    @classmethod
    def all(cls) -> List["Alert"]:
        alerts_from_db = Database.find("alerts", {})
        return [cls(**alert) for alert in alerts_from_db]
    
    def save_to_mongo(self) -> None:
        Database.insert(self.collection, self.json())
