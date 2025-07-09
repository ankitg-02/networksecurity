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

class Networkdataextraction:
    def __init__(self):
        try:
            pass
        except Exception as e:
            