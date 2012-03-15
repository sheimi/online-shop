from flask import Flask, g, session
from flask_peewee.db import Database
from views.admin import Admin
from views.rest import RestAPI, UserAuthentication
from views.auth import Auth

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

def register_module():
    from views.core import core
    from views.member import member
    from views.commodity import commodity
    from views.cart import cart
    from views.admina import admina
    from models import register_commodity, register_core, register_order

    app.register_blueprint(member, url_prefix='/member')
    app.register_blueprint(core, url_prefix='/core')
    app.register_blueprint(commodity, url_prefix='/commodity')
    app.register_blueprint(cart, url_prefix='/cart')
    app.register_blueprint(admina, url_prefix='/admina')

    register_order(admin=admin, api=api)
    register_commodity(admin=admin, api=api)
    register_core(admin=admin, api=api)
    admin.setup()
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
