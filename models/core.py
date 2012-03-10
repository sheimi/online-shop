from shop import db

class Member(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    discount = db.Column(db.Integer)

    users = db.relationship('User', backref='membership', lazy='dynamic')

    def __init__(self, name, discount=100):
        self.name = name
        self.discount = discount

    def __repr__(self):
        return "<Member ('%s')>" % (self.name)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    membership_id = db.Column(db.Integer, db.ForeignKey('member.id'))


    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return "<User('%s')>" % (self.username)

