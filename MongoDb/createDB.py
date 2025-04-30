import pymongo

myclient = pymongo.MongoClient("mongodb+srv://stewie:onetoeight18@cluster0.idrdxfd.mongodb.net/")

mydb = myclient["mydatabase"]