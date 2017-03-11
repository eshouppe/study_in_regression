"""Functions the insert or query db. Also any processing of content
received from / sent to db"""
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.test_db
cllctn = db.test_cllctn

