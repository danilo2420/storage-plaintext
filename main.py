from flask import Flask
from database.database import testDatabaseConnection
from blueprints.users.users import users_bp
from blueprints.singers.singers import singers_bp

if not testDatabaseConnection():
    exit()

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(singers_bp)

@app.route("/")
def test():
    return "I'm up and running!", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")