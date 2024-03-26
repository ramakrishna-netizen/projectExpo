from app import db



class User(db.Model):


    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable = False, unique=True)
    password = db.Column(db.String(120), nullable = False)
    image_file = db.Column(db.String(120), default='default.jpeg', nullable=False)

    def __repr__(self):
        return f'Name:{self.name} Email:{self.email} Pass:{self.password} image:{self.image_file}'