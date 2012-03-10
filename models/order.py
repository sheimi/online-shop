from shop import db
from datetime import datetime as dt

class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    create_date   = db.Column(db.DateTime)      #date the order created
    confirm_date  = db.Column(db.DateTime)      #date the order confirmed 
    complete_date = db.Column(db.DateTime)         #date the order will be sent


    is_confirmed = db.Column(db.Boolean)        #is confirmed   turn cart into an real order
    is_complete  = db.Column(db.Boolean)        #is the order conplete

    status = db.Column(db.Integer)              #0: init  1: confirmed 2: ... 3: ...

    discount = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='orders')
    
    items = db.relationship('OrderItem', backref='order')

    def __init__(self, user, discount=100):

        self.create_date = dt.now()
        self.user = user 
        self.discount = discount

        self.is_complete    = False
        self.is_confirmed   = False

    def __repr__(self):
        return "<Order %d>" % self.id

    def total_price(self):
        return sum([x.total_price() for x in self.items])



class OrderItem(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    price = db.Column(db.Integer)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    commodity_id = db.Column(db.Integer, db.ForeignKey('commodity.id'))
    commodity = db.relationship('Commodity', backref='order_items')

    def __init__(self, order, commodity, num, price):
        self.num = num
        self.price = price

        self.order = order
        self.commodity = commodity

    def __repr__(self):
        return '<Order Item>'

    def total_price(self):
        return self.num * self.price
