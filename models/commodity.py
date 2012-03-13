from shop import db
from peewee import *
from models.core import User
import datetime

class Category(db.Model):
    
    name = CharField()
    parent = ForeignKeyField('self', related_name='children', null=True)

    def __repr__(self):
        return "<Category ('%s')>" % (self.name)


class Commodity(db.Model):

    name = CharField()
    price = IntegerField(default=100)
    des = TextField(default="This is the Description")

    category = ForeignKeyField(Category, related_name='commodities', null=True)
    
    def __repr__(self):
        return "<Commodity ('%s')>" % (self.name)

    def avg_rating(self):
        ratings = [x.rating for x in self.comments]
        avg_rating = sum(ratings) * 1.0 / len(ratings)
        return round(avg_rating, 1)
    
class CommodityImage(db.Model):
    
    name = CharField()
    commodity = ForeignKeyField(Commodity, related_name='imgs')

class CommodityComment(db.Model):

    comment = TextField(default="This is the Comment")
    user = ForeignKeyField(User, related_name='comments')
    commodity = ForeignKeyField(Commodity, related_name='comments')
    date = DateTimeField(default=datetime.datetime.now)
    rating = IntegerField(default=3)
