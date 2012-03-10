from flask import Flask, g, session
from flaskext.sqlalchemy import SQLAlchemy
from views import *

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SQLALCHEMY_DATABASE_URI='sqlite:///models/shop.db',
    SECRET_KEY = 'development key',
    #SQLALCHEMY_ECHO=True,
)

db = SQLAlchemy(app)

app.register_blueprint(member, url_prefix='/member')
app.register_blueprint(core, url_prefix='/core')

@app.before_request
def before_request():
    from models import User
    if 'user_id' in session:
        g.user = User.query.get(int(session['user_id']))
    else:
        g.user = None

if __name__ == '__main__':
    app.run()
