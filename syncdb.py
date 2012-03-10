from shop import db
from models import *

def init_db():
    #init user
    user = User("sheimi", "zhang", True)
    db.session.add(user)
    db.session.commit()

    #init Member
    member = Member("vip1")
    db.session.add(member)
    db.session.commit()
    member.users.append(user)
    db.session.commit()

    #init Commodity
    cat = Category("c1")
    db.session.add(cat)
    co = Commodity("co1")
    db.session.add(co)
    db.session.commit()
    co.category = cat
    db.session.commit()

    #init order
    order = Order(user)
    db.session.add(order)
    db.session.commit()
    oi = OrderItem(order, co, 10, 10)
    db.session.add(oi)
    db.session.commit()
    

    

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    init_db()
