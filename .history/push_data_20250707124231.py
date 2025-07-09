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
        
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json_loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)    
         
    def push_data_to_mongodb(self, records, collection,database):        