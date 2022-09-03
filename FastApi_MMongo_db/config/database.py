
from pymongo import MongoClient






client = MongoClient("mongodb+srv://mahabub866:mahabub866@cluster0.hma8fd2.mongodb.net/?retryWrites=true&w=majority")




db = client.todo_application

collection_name = db["todos_app"]