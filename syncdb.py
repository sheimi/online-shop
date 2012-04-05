#!/bin/env python
from models.core import User, Member, Address
from models.attachment import Announcement, Feedback
from models.commodity import Category, Commodity, CommodityImage, \
                             CommodityComment
from models.order import OrderStatus, UserOrder, OrderItem
from datetime import datetime as dt
import string
import random


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

    CommodityImage.drop_table()
    CommodityImage.create_table()

    CommodityComment.drop_table()
    CommodityComment.create_table()

    Address.drop_table()
    Address.create_table()

    OrderStatus.drop_table()
    OrderStatus.create_table()

    Announcement.drop_table()
    Announcement.create_table()
    Feedback.drop_table()
    Feedback.create_table()


def random_name(bit, bit_min=0, min_l=2, max_l=6):
    for b in range(bit_min, bit):
        yield ''.join(random.choice(string.ascii_letters) \
                      for x in range(random.randint(min_l, max_l)))


def random_img():
    img = ['Fresh_Fruit_dessert_photo_JT002_350A1024768.jpg',
           'Valentine-dessert2.jpg',
           'Fruit_dessert_eastern.jpg',
           'chocolate-fruit-n-nut-cases200812311.jpg',
           'Ice_Cream_dessert_02.jpg',
           'elegantlemonjellocreamdessertc2a9m-'
           'jdemesterton8-29-201012-54-30pm.jpg',
           'Summer_Fruit_Dessert.jpg',
           'ua-chocolate-delight-dessert-1067.JPG']
    return random.choice(img)


status_list = []
memberships = []
category_list = []
co_list = []
user_list = []


def random_feed():
    user = random.choice(user_list)
    content = ' '.join(random_name(10))
    feed = Feedback.create(user=user, content=content)
    return feed


def random_user():
    global memberships
    global user_list
    username = ' '.join(random_name(2))
    password = 'zhang'
    user = User.create(username=username, password=password,
                       membership=random.choice(memberships))
    #user.set_password("zhang")
    #user.save()
    user_list.append(user)
    return user


def random_cat():
    global category_list
    name = ' '.join(random_name(1))
    cat = Category.create(name=name, parent=random.choice(category_list))
    category_list.append(cat)
    return cat


def random_co():
    global category_list
    global co_list
    name = ' '.join(random_name(1))
    co = Commodity.create(price=random.randint(20, 100), name=name,
                          category=random.choice(category_list))
    CommodityImage.create(name=random_img(), commodity=co)
    co_list .append(co)
    return co


def random_oi(order):
    global co_list
    co = random.choice(co_list)
    num = random.randint(1, 4)
    price = co.price
    oi = OrderItem.create(commodity=co, num=num, price=price, order=order)
    return oi


def random_order(user):
    global status_list
    status = random.choice(status_list)
    kwargs = {
        'user': user,
        'status': status,
    }
    if not status.name == "init":
        kwargs['is_confirmed'] = True
        kwargs['confirm_date'] = dt.today()
    if status.name == "complete" or status.name == "canceled":
        kwargs['is_compelete'] = True
        kwargs['compelete_date'] = dt.today()
    order = UserOrder.create(**kwargs)
    for i in range(2, 10):
        random_oi(order)
    return order


def init_db():
    #init status
    global status_list
    global memberships
    global category_list
    global user_list

    s_init = OrderStatus.create(name="init")
    s_confirmed = OrderStatus.create(name="confirmed")
    s_sent = OrderStatus.create(name="sent")
    s_complete = OrderStatus.create(name="complete")
    s_canceled = OrderStatus.create(name="canceled")
    status_list += [s_init, s_confirmed, s_sent, s_complete, s_canceled]

    member0 = Member.create(name="normal", point=1000, discount=100)
    member1 = Member.create(name="vip1", point=2000,  discount=90)
    member2 = Member.create(name="vip2", point=3000, discount=80)
    member3 = Member.create(name="vip3", point=4000, discount=70)
    member4 = Member.create(name="vip4", point=5000, discount=60)
    member5 = Member.create(name="vip5", point=-1, discount=50)
    memberships += [member1, member2, member3, member4]

    #init user
    User.create(username="sheimi", password="zhang", admin=True)
    #user = User.create(username="sheimi", password="zhang", admin=True)
    #user.set_password("zhang")
    #user.save()

    Announcement.create(title="Hello", content="World")
    Announcement.create(title="Hello", content="World")
    Announcement.create(title="Hello", content="World")

    for i in range(100):
        random_user()

    #init Commodity
    cat = Category.create(name="All")
    category_list.append(cat)
    for i in range(10):
        random_cat()

    for i in range(100):
        random_co()

    for u in user_list:
        random_order(u)

    for i in range(20):
        random_feed()

if __name__ == '__main__':
    create_db()
    init_db()
