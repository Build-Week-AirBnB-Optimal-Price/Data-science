from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Listing(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)
    host_since = DB.Column(DB.String(50), nullable=False) # convert to date_time
    zipcode = DB.Column(DB.Integer, nullable=False)
    room_type = DB.Column(DB.String(30), nullable=False)
    max_nights = DB.Column(DB.Integer, nullable=False)
    min_nights = DB.Column(DB.Integer, nullable=False)
    extra_people = DB.Column(DB.Integer, nullable=False)
    accomodates = DB.Column(DB.Integer, nullable=False)
    neighborhood = DB.Column(DB.String(50), nullable=False)
    beds = DB.Column(DB.Integer, primary_key=True)
    property_type = DB.Column(DB.String(50), nullable=False)
    cancel_policy = DB.Column(DB.String(200), nullable=False)
    guests = DB.Column(DB.Integer, nullable=False)
    bedrooms = DB.Column(DB.Integer, nullable=False)
    bathrooms = DB.Column(DB.Integer, primary_key=True)

    def __repr__(self):
        return '<Listing {}>'.format(self.name)