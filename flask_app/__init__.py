from flask import Flask, session
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
bcrypt = Bcrypt(app)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')


# openssl rand -hex 32 =>
# creates a algorithm of random numbers for you to create a secret key
app.secret_key = "8705aebb510b4ba87cef64e04c11f0ea4dd4ece78e5a9718b9d409c4ffc7e062" 

