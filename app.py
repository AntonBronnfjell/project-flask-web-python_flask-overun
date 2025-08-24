from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from routes import *  # noqa: E402,F401


if __name__ == '__main__':
    # Create tables automatically on startup
    with app.app_context():
        db.create_all()
    app.run(debug=True)


