from shop import db
from peewee import *
from views.auth import BaseUser
import datetime

class Member(db.Model):

    name = CharField()
    discount = IntegerField(default=100)

    def __repr__(self):
        return "<Member ('%s')>" % (self.name)

class User(db.Model, BaseUser):

    username = CharField(null=False)
    password = CharField(null=False)
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    age = IntegerField(default=0)
    address = CharField(null=True)
    gender = IntegerField(default=0) #0: secrete,  1: boy   2: girl

    membership = ForeignKeyField(Member, related_name='users', null=True)

    def __repr__(self):
        return "<User('%s')>" % (self.username)

