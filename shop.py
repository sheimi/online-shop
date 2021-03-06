#!/bin/env python
from flask import Flask, g, session
from flask_peewee.db import Database
from views.admin import Admin
from views.rest import RestAPI, UserAuthentication
from views.auth import Auth
from settings import settings

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='development key',
    DATABASE={
        'name': settings['database']['name'],
        'engine': 'peewee.SqliteDatabase' if settings['database']['type'] == 'sqlite3' else None,
    },
    INDEX_DIR=settings['indexdir'],
)

app.jinja_env.globals['globals'] = {
    'appname': settings['appname'],
    'im_host': settings['im_host'],
    'forum_host': settings['forum_host'],
}

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
    from views.feedback import feedback
    from models.commodity import register_commodity
    from models.core import register_core
    from models.order import register_order
    from models.attachment import register_attachment

    app.register_blueprint(member, url_prefix='/member')
    app.register_blueprint(commodity, url_prefix='/commodity')
    app.register_blueprint(cart, url_prefix='/cart')
    app.register_blueprint(admina, url_prefix='/admina')
    app.register_blueprint(feedback, url_prefix='/feedback')
    app.register_blueprint(core, url_prefix='/core')
    app.register_blueprint(core, url_prefix='/')

    register_order(admin=admin, api=api)
    register_commodity(admin=admin, api=api)
    register_core(admin=admin, api=api)
    register_attachment(admin=admin, api=api)
    admin.setup()
    api.setup()


@app.before_request
def before_request():
    from models.core import User
    if 'user_pk' in session:
        try:
            g.user = User.select().get(id=int(session['user_pk']))
        except:
            g.user = None
    else:
        g.user = None

if __name__ == '__main__':
    register_module()
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(settings['port'])
    IOLoop.instance().start()
    #app.run()
