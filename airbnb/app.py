from decouple import config
from flask import Flask, render_template, request
# from .models import DB

app = Flask(__name__)
# APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airbnb_db.sqlite3'
# DB = SQLAlchemy(APP)

@app.route('/')
def root():
    # DB.create_all()
    return render_template('base.html', title='Home')