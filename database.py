from pymongo import MongoClient
import sys
from dotenv import load_dotenv
import os

if "--test" in sys.argv:
    load_dotenv(override=True, dotenv_path="./.env.local")

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_DOMAIN = os.getenv("MONGO_DOMAIN")
MONGO_PORT = os.getenv("MONGO_PORT")

URL=f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_DOMAIN}{MONGO_PORT}"
print(f"Database URL is {URL}")

client = MongoClient(URL)

def testDatabaseConnection():
    try:
        client.admin.command('ismaster')
        print("Database connection was successful")
        return True
    except Exception as e:
        print(f"Database connection failed. An exception occurred: {e}")
        return False
