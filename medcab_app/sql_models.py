from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

db = SQLAlchemy()

migrate = Migrate()

class Strain(db.Model):
    id = db.Column(db.Integer, primary_key=False)
    strain = db.Column(db.String)
    rating = db.Column(db.Float)
