from decouple import config
from flask import Flask, render_template, request
# from .models import DB

# app = Flask(__name__)
# APP.config['SQLALCHEM Y_DATABASE_URI'] = 'sqlite:///airbnb_db.sqlite3'
# DB = SQLAlchemy(APP)

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        # DB.create_all()
        return render_template('base.html', title='Home')