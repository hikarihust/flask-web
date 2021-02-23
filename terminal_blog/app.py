import pymongo

URI = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(URI)
database = client['fullstack']
collection = database['students']

students = [student["mark"] for student in collection.find({}) if student["mark"] == 99.0]

print(students)