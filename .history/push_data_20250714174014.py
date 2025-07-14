import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL= os.getenv("MONGO_DB_URL")

print("MONGO_DB_URL:", MONGO_DB_URL)

import certifi
ca= certifi.where()

import pandas as pd
import numpy as np
import pymongo
from netwroksecurity.exception.exception import NetworkSecurityException
from netwroksecurity.logging.logger import logging

class NetworkDataExtraction:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())  # fixed typo here
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def push_data_to_mongodb(self, records, collection, database):
        try:
            print("Connecting to database:", database)
            print("Target collection:", collection)
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            db = self.mongo_client[database]
            col = db[collection]
            result = col.insert_many(records)
            print("Inserted IDs:", result.inserted_ids[:5], "...")  # print first 5 IDs
            print("Total inserted:", len(result.inserted_ids))
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
        
if __name__ == "__main__":
    FILEPATH = r'Network_Data\phisingData.csv'  # use raw string to avoid escape sequence warning
    DATABASE = 'ANKIT_PROJECT'
    COLLECTION = 'Network_Data'
    networkobject = NetworkDataExtraction()
    records = networkobject.csv_to_json_convertor(FILEPATH)
    no_of_records = networkobject.push_data_to_mongodb(records, COLLECTION, DATABASE)
    print(no_of_records, "records inserted successfully into the database.")
    print("Inserting into database:", DATABASE)
    print("Inserting into collection:", COLLECTION)
