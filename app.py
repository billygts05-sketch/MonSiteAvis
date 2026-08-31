import os

from dotenv import load_dotenv
from flask import Flask

from database import creer_table
from routes.pin import pin_bp

app = Flask(__name__)

load_dotenv()

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ["SECRET_KEY"]

app.register_blueprint(pin_bp)

if __name__=="__main__" :
    creer_table()
    app.run(debug=True)