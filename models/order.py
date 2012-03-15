from shop import db
from peewee import *
from datetime import datetime as dt
from models.core import User, Address
from models.commodity import Commodity
from views.admin import ModelAdmin

class OrderStatus(db.Model):
    name = CharField(null=False)

    def __unicode__(self):
        return "%s" % (self.name)


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
    status = ForeignKeyField(OrderStatus, related_name='orders', default=1)

    def total_price(self):
        return sum([x.total_price() for x in self.items])

    def __unicode__(self):
        return "#%s" % (self.id)

class OrderItem(db.Model):
    
    num = IntegerField()
    price = IntegerField()

    commodity = ForeignKeyField(Commodity, related_name='order_items', null=True)
    order = ForeignKeyField(UserOrder, related_name='items', null=True)

    def total_price(self):
        return self.num * self.price


class UserOrderAdmin(ModelAdmin):
    columns = ('id', 'user', 'status')

class OrderItemAdmin(ModelAdmin):
    columns = ('commodity', 'order')


#register stuff
def register_order(**regs):
    regs['admin'].register(UserOrder, UserOrderAdmin)
    regs['admin'].register(OrderItem, OrderItemAdmin)
    
    regs['api'].register(UserOrder)
    regs['api'].register(OrderItem)


