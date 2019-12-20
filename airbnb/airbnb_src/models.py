from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Listing(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)
    summary = DB.Column(DB.String(200), nullable=True)
    neighborhood = DB.Column(DB.String(30), nullable=True)
    bedrooms = DB.Column(DB.Integer, primary_key=True)
    beds = DB.Column(DB.Integer, primary_key=True)
    bathrooms = DB.Column(DB.Integer, primary_key=True)

    def __repr__(self):
        return '<Listing {}>'.format(self.name)