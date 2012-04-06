from shop import db
from peewee import CharField, IntegerField, TextField,\
                   DateTimeField, ForeignKeyField
from models.core import User
import datetime
from views.admin import ModelAdmin


class Category(db.Model):

    name = CharField()
    parent = ForeignKeyField('self', related_name='children', null=True)

    def __unicode__(self):
        return "%s" % self.name

    def get_children(self):
        result = []

        def get_ch(child):
            if child.children.count() == 0:
                result.append(child.id)
                return
            it = iter(child.children)
            try:
                while True:
                    get_ch(it.next())
            except StopIteration:
                result.append(child.id)
                return

        get_ch(self)
        import json
        return json.dumps(result)


class Commodity(db.Model):

    name = CharField()
    price = IntegerField(default=100)
    des = TextField(default="This is the Description")
    join_date = DateTimeField(default=datetime.datetime.now)

    category = ForeignKeyField(Category, related_name='commodities', null=True)

    def __unicode__(self):
        return "%s" % self.name

    def avg_rating(self):
        ratings = [x.rating for x in self.comments]
        if not ratings:
            return "There are not comment"
        avg_rating = sum(ratings) * 1.0 / len(ratings)
        return round(avg_rating, 1)

    def is_category(self, cat):
        if cat == 1:
            return True
        c = self.category
        while c.id != 1:
            if c.id == cat:
                return True
            c = c.parent
        return False

class CommodityImage(db.Model):

    name = CharField()
    commodity = ForeignKeyField(Commodity, related_name='imgs')


class CommodityComment(db.Model):

    comment = TextField(default="This is the Comment")
    user = ForeignKeyField(User, related_name='comments')
    commodity = ForeignKeyField(Commodity, related_name='comments')
    date = DateTimeField(default=datetime.datetime.now)
    rating = IntegerField(default=3)


class CategoryAdmin(ModelAdmin):
    columns = ('name', 'parent')


class CommodityAdmin(ModelAdmin):
    columns = ('name', 'category')


class CommodityCommentAdmin(ModelAdmin):
    columns = ('user', 'commodity', 'comment')


class CommodityImageAdmin(ModelAdmin):
    columns = ('commodity')


#register stuff
def register_commodity(**regs):
    regs['admin'].register(Category, CategoryAdmin)
    regs['admin'].register(Commodity, CommodityAdmin)
    regs['admin'].register(CommodityComment, CommodityCommentAdmin)
    regs['admin'].register(CommodityImage)

    regs['api'].register(Category)
    regs['api'].register(Commodity)
    regs['api'].register(CommodityComment)
