from shop import db
from peewee import *

class Category(db.Model):
    
    name = CharField()
    parent = ForeignKeyField('self', related_name='children', null=True)

    def __repr__(self):
        return "<Category ('%s')>" % (self.name)


class Commodity(db.Model):

    name = CharField()

    category = ForeignKeyField(Category, related_name='commodities', null=True)
    
    def __repr__(self):
        return "<Commodity ('%s')>" % (self.name)
    

