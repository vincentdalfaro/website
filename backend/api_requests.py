from db_store import collection
from enable_log import logger
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

logger.info("in api_requests")

collection_data = collection.find()

for item in collection_data:
    print(item)
