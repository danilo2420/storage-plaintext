from flask import Flask
import sys
from dotenv import load_dotenv
from database import testDatabaseConnection

if not testDatabaseConnection():
    exit()

if "--test" in sys.argv:
    print("Loading environment variables from .env file")
    load_dotenv(override=True)

app = Flask(__name__)

@app.route("/")
def test():
    return "I'm up and running!", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")