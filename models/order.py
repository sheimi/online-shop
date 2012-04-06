from shop import db
from peewee import CharField, IntegerField, BooleanField,\
                   DateTimeField, ForeignKeyField
from models.core import User, Address
from models.commodity import Commodity
from views.admin import ModelAdmin


class OrderStatus(db.Model):
    name = CharField(null=False)

    def __unicode__(self):
        return "%s" % (self.name)


class UserOrder(db.Model):
    #date the order created
    #date the order confirmed reate_date = DateTimeField(default=dt.now)
    confirm_date = DateTimeField(null=True)
    #date the order will be sent
    complete_date = DateTimeField(null=True)

    #is confirmed   turn cart into an real order
    is_confirmed = BooleanField(default=False)
    #is the order conplete
    is_complete = BooleanField(default=False)
    #1: init  2: confirmed 3: sent 4: completed 5:canceled
    status = IntegerField(default=0)
    discount = IntegerField(default=100)

    user = ForeignKeyField(User, related_name='orders', null=True)
    address = ForeignKeyField(Address, related_name='orders', null=True)
    status = ForeignKeyField(OrderStatus, related_name='orders', default=1)

    def total_price(self):
        return self.total_price_raw() * self.discount / 100

    def total_price_raw(self):
        return sum([x.total_price() for x in self.items])

    def __unicode__(self):
        return "#%s" % (self.id)


class OrderItem(db.Model):

    num = IntegerField()
    price = IntegerField()

    commodity = ForeignKeyField(Commodity, related_name='order_items',
                                null=True)
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
