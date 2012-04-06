from shop import db
from peewee import CharField, IntegerField, BooleanField,\
                   DateTimeField, ForeignKeyField
from views.auth import BaseUser
import datetime
from views.admin import ModelAdmin


class Member(db.Model):

    name = CharField()
    point = IntegerField(default=0)
    discount = IntegerField(default=100)

    def __unicode__(self):
        return "%s" % (self.name)


class User(db.Model, BaseUser):

    username = CharField(null=False)
    password = CharField(null=False)
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    age = IntegerField(default=0)
    address = CharField(null=True)
    #0: secrete, 1: boy, 2: girl
    gender = IntegerField(default=0)
    point = IntegerField(default=0)

    membership = ForeignKeyField(Member, related_name='users', null=True)

    def __unicode__(self):
        return "%s" % (self.username)

    def has_comment(self, commodity):
        return self.comments.filter(commodity__id=commodity.id).count() > 0

    def can_comment(self, commodity):
        print commodity.order_items.filter(order__user__id=self.id).count() 
        return commodity.order_items.filter(order__user__id=self.id,
                                            order__status=4)\
                                    .count() > 0 and not\
                                    self.has_comment(commodity)

    def check_membership(self):
        members = list(Member.select().order_by("point"))[1:]
        for member in members:
            if self.point < member.point:
                return member
        return members[-1]

class Address(db.Model):
    columns = ('user', 'address',)

    user = ForeignKeyField(User, related_name='addresses')
    name = CharField(null=False)
    address = CharField(null=False)
    zipcode = CharField(null=False)
    phone = CharField(null=False)

    def __unicode__(self):
        return "%s " % (self.user)


class MemberAdmin(ModelAdmin):
    columns = ('name', 'discount')


class UserAdmin(ModelAdmin):
    columns = ('username', 'active', 'membership')


class AddressAdmin(ModelAdmin):
    columns = ('user', 'address')


def register_core(**regs):
    regs['admin'].register(Address, AddressAdmin)
    regs['admin'].register(User, UserAdmin)
    regs['admin'].register(Member, MemberAdmin)

    regs['api'].register(Address)
    regs['api'].register(User)
    regs['api'].register(Member)
