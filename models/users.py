from settings.extensions import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    addresses = db.Column(db.String(999))