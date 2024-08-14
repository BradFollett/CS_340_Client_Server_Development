from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU2024'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30345
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, searchData):
        # Check if searchData is provided
        if searchData: 
            # If searchData is provided, perform a find operatoin with the provided query
            # Exlcude the _id field from the result
            data = self.database.animals.find(searchData, {"_id": False})
        else: 
            # If searchData is not provided, perform a find operation without any query
            # Exlcude the _id field from the result
            data = self.database.animals.find({}, {"_id": False})
        return data
    
#Create method to implement the U in CRUD.
    def update(self, searchData, updateData):
        # Check if 'searchData' is provided
        if updateData is not None:
            # If 'searchData' is provided, execute an update operation in the 'animals' collection of the MongoDB database
            # Update all documents matching the 'searchData' query with the 'updateData' values
            result = self.database.animals.update_many(searchData, {"$set": updateData})
        else:
            # If 'searchData' is not provided, return an empty dictionary
            return "{}"
        # Return the raw result of the update operation
        return result.raw_result

# Create method to implement the D in CRUD.
    def delete(self, deleteData):
        # Check if 'deleteData' is provided
        if deleteData is not None:
            # If 'deleteData' is provided, execute a delete operation in the 'animals' collection of the MongoDB database
            # Delete all documents matching the 'deleteData' query
            result = self.database.animals.delete_many(deleteData)
        else:
            # If 'deleteData' is not provided, return an empty dictionary
            return "{}"
        # Return the raw result of the delete operation
        return result.raw_result




   