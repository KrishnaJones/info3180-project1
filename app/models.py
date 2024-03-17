from . import db

class Property(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(800))
    num_of_bedrooms = db.Column(db.Integer)
    num_of_bathrooms = db.Column(db.Integer)
    price = db.Column(db.Float)
    type = db.Column(db.String(40))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(80))
    
    

    def __init__(self, title, description, num_of_bedrooms, num_of_bathrooms, price, type, location, photo):
        self.title = title
        self.description = description
        self.num_of_bedrooms = num_of_bedrooms
        self.num_of_bathrooms = num_of_bathrooms
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)