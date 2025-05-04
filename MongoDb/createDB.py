import pymongo

myclient = pymongo.MongoClient("mongodb+srv://stewie:onetoeight18@cluster0.idrdxfd.mongodb.net/")

mydb = myclient["mydatabase"]

# checking if the database exists

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("The database does not exist.")