
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://stewie:onetoeight18@cluster0.idrdxfd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
#creating a db
mydb = client["mydatabase"]
#creating a collection
mycol = mydb["customers"]

# checking if the database exists
dblist = client.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")