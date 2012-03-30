from shop import db
from peewee import CharField, ForeignKeyField, TextField
from models.core import User


class Announcement(db.Model):

    title = CharField()
    content = TextField()

    def __unicode__(self):
        return "%s" % (self.title)


class Feedback(db.Model):

    content = TextField()
    user = ForeignKeyField(User, related_name='feedbacks', null=True)

    def __unicode__(self):
        return "%s" % (self.content)


def register_attachment(**regs):
    regs['admin'].register(Feedback)
    regs['admin'].register(Announcement)

    regs['api'].register(Announcement)
    regs['api'].register(Feedback)
