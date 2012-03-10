from shop import db

class Commodity(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Commodity ('%s')>" % (self.name)
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    children = db.relationship('Category', backref=db.backref('parent', remote_side=[id]))

    commodities = db.relationship('Commodity', backref='category', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category ('%s')>" % (self.name)


