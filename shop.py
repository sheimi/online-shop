from flask import Flask, g, session
from views import *
from flask_peewee.db import Database
from flask_peewee.admin import Admin
from flask_peewee.auth import Auth
from flask_peewee.rest import RestAPI, UserAuthentication

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

auth = Auth(app, db)
admin = Admin(app, auth)
api = RestAPI(app, default_auth=UserAuthentication(auth))
def register_admin():
    from models import User, Member, UserOrder, OrderItem, Category, Commodity
    admin.register(User)
    admin.register(Member)
    admin.register(UserOrder)
    admin.register(OrderItem)
    admin.register(Category)
    admin.register(Commodity)
    admin.setup()

def register_rest():
    from models import User, Member, UserOrder, OrderItem, Category, Commodity
    api.register(User)
    api.register(Member)
    api.register(UserOrder)
    api.register(OrderItem)
    api.register(Category)
    api.register(Commodity)
    api.setup()



app.register_blueprint(member, url_prefix='/member')
app.register_blueprint(core, url_prefix='/core')

@app.before_request
def before_request():
    from models import User
    if 'user_pk' in session:
        g.user = User.select().get(id=int(session['user_pk']))
    else:
        g.user = None

if __name__ == '__main__':
    register_admin()
    register_rest()
    app.run()
