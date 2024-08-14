from pymongo import MongoClient, ASCENDING, DESCENDING
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, passwd):
        # Connection Variables
        USER = username
        PASS = passwd
        HOST = 'localhost'
        PORT = 30345
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]
        
        # Create indexes
        self.create_indexes()

    def create_indexes(self):
        self.collection.create_index([('animal_id', ASCENDING)], unique=True)
        self.collection.create_index([('name', ASCENDING)])
        self.collection.create_index([('breed', ASCENDING)])
        self.collection.create_index([('location_lat', ASCENDING), ('location_long', ASCENDING)])
        self.collection.create_index([('sex_upon_outcome', ASCENDING)])
        self.collection.create_index([('age_upon_outcome_in_weeks', ASCENDING)])
        self.collection.create_index([('outcome_type', ASCENDING)])

    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, searchData):
        if searchData:
            data = self.collection.find(searchData, {"_id": False})
        else:
            data = self.collection.find({}, {"_id": False})
        return data

    def update(self, searchData, updateData):
        if updateData is not None:
            result = self.collection.update_many(searchData, {"$set": updateData})
        else:
            return "{}"
        return result.raw_result

    def delete(self, deleteData):
        if deleteData is not None:
            result = self.collection.delete_many(deleteData)
        else:
            return "{}"
        return result.raw_result
