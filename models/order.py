from shop import db
from peewee import *
from datetime import datetime as dt
from models.core import User, Address
from models.commodity import Commodity

class UserOrder(db.Model):


    create_date   = DateTimeField(default=dt.now)       #date the order created
    confirm_date  = DateTimeField(null=True)         #date the order confirmed 
    complete_date = DateTimeField(null=True)         #date the order will be sent


    is_confirmed = BooleanField(default=False)          #is confirmed   turn cart into an real order
    is_complete  = BooleanField(default=False)          #is the order conplete

    status = IntegerField(default=0)              #0: init  1: confirmed 2: sent 3: completed 4:canceled 
    discount = IntegerField(default=100)

    user = ForeignKeyField(User, related_name='orders', null=True)
    address = ForeignKeyField(Address, related_name='orders', null=True) 

    def total_price(self):
        return sum([x.total_price() for x in self.items])


class OrderItem(db.Model):
    
    num = IntegerField()
    price = IntegerField()

    commodity = ForeignKeyField(Commodity, related_name='order_items', null=True)
    order = ForeignKeyField(UserOrder, related_name='items', null=True)

    def total_price(self):
        return self.num * self.price
