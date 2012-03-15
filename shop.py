from flask import Flask, g, session
from flask_peewee.db import Database

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SQLALCHEMY_DATABASE_URI='sqlite:///models/shop.db',
    SECRET_KEY = 'development key',
    DATABASE = {
        'name'  :   'models/shop.db',
        'engine':   'peewee.SqliteDatabase',
    },
)

db = Database(app)

def register_module():
    from views import Admin, RestAPI, UserAuthentication, Auth, core, member, commodity, cart
    from models import User, Member, UserOrder, OrderItem, Category, Commodity, CommodityComment, Address

    app.register_blueprint(member, url_prefix='/member')
    app.register_blueprint(core, url_prefix='/core')
    app.register_blueprint(commodity, url_prefix='/commodity')
    app.register_blueprint(cart, url_prefix='/cart')
    auth = Auth(app, db)
    admin = Admin(app, auth)
    api = RestAPI(app, default_auth=UserAuthentication(auth))

    admin.register(User)
    admin.register(Member)
    admin.register(UserOrder)
    admin.register(OrderItem)
    admin.register(Category)
    admin.register(Commodity)
    admin.register(Address)
    admin.register(CommodityComment)
    admin.setup()

    api.register(User)
    api.register(Member)
    api.register(UserOrder)
    api.register(OrderItem)
    api.register(Category)
    api.register(Commodity)
    api.register(CommodityComment)
    api.register(Address)
    api.setup()

@app.before_request
def before_request():
    from models import User
    if 'user_pk' in session:
        try:
            g.user = User.select().get(id=int(session['user_pk']))
        except:
            g.user = None
    else:
        g.user = None

if __name__ == '__main__':
    register_module()
    app.run()
