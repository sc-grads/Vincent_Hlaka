from flask_cors import CORS
CORS(app)
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'

