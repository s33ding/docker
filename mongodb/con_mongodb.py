import json
import os
from shared_func_mongo import * 

client = connect_to_mongodb()
db = client["nobel"]
