import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)