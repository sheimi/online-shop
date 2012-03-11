from shop import db
from models import *
from peewee import *

def create_db():
    User.drop_table()
    User.create_table()

    Member.drop_table()
    Member.create_table()

    Commodity.drop_table()
    Commodity.create_table()

    Category.drop_table()
    Category.create_table()

    UserOrder.drop_table()
    UserOrder.create_table()

    OrderItem.drop_table()
    OrderItem.create_table()

def init_db():
    #init user
    user = User.create(username="sheimi", password="zhang", admin=True)
    #user.set_password("zhang")
    #user.save()
    
    user2 = User.create(username="sheimi2", password="zhang", admin=True)
    #user2.set_password("zhang")
    #user2.save()

    #init Member
    member = Member.create(name="vip1")
    user.membership = member
    user.save()

    #init Commodity
    cat = Category.create(name="c1")
    co = Commodity.create(name="co1")
    co.category = cat
    co.save()

    #init order
    order = UserOrder.create(user=user)
    oi = OrderItem.create(order=order, commodity=co, num=10, price=10)
    

if __name__ == '__main__':
    create_db()
    init_db()
