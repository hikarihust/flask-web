import pymongo

URI = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(URI)
database = client['fullstack']
collection = database['students']

students = collection.find({})

print(students)
for student in students:
    print(student)
    