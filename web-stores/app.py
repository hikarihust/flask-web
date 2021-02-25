from models.item import Item
from models.alert import Alert


ipad = Item(
    "https://www.johnlewis.com/2020-apple-ipad-pro-11-inch-a12z-bionic-ios-wi-fi-1tb/space-grey/p4949061",
    "p",
    {"class": "price price--large"}
)

ipad.save_to_mongo()

alert = Alert(ipad._id, 2000)
alert.save_to_mongo()
