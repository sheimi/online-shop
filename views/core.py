from flask import Blueprint, render_template, g, session, jsonify, request,\
        redirect, url_for
from util.auth import get_object_or_404
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from peewee import Q
from models.commodity import Commodity, Category
from models.attachment import Announcement
from models.core import User

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('core/index.html', index=True, user=g.user)


@core.route('/recommend')
def recommend():
    recommends = list(Commodity.select())[0:10]
    return render_template('core/gallery_view.html',
                            title="Recommendation",
                            items=recommends, id="rec")


@core.route('/get-hot')
def get_hot():
    coms = list(Commodity.select())
    result = sorted(coms, key=lambda a: a.order_items.count(), reverse=True)
    if len(result) > 5:
        result = result[:5]
    return render_template('core/gallery_view.html', items=result,
                                    title="What's Host", id="hot")


@core.route('/get-new')
def get_new():
    coms = list(Commodity.select())
    result = sorted(coms, key=lambda a: a.join_date, reverse=True)
    if len(result) > 5:
        result = result[:5]
    return render_template('core/gallery_view.html', items=result,
                            title="What's New", id="new")


@core.route('/get-anno')
def get_anno():
    annos = list(Announcement.select())
    annos = annos[-5:]
    return render_template('core/annos.html', annos=annos)


@core.route('/result')
def result():
    query = request.args.get('q', None)
    return render_template('core/result.html', query=query)


@core.route('/com-list')
def com_list():
    commodities = Commodity.select().filter(**request.args)
    return render_template('core/com_list.html', commodities=commodities)


@core.route('/com-filter-list')
def com_filter_list():
    categories = Category.select().filter(**request.args)
    return render_template('core/com_filter_list.html', categories=categories)


@core.route('/compare-box')
def compare_box():
    c1 = get_object_or_404(Commodity, id=request.args.get("c1"))
    c2 = get_object_or_404(Commodity, id=request.args.get("c2"))
    return render_template('core/compare_box.html', c1=c1, c2=c2)


@core.route('/search')
def search_commodity():
    from shop import app
    ix = open_dir(app.config.get("INDEX_DIR"))
    searcher = ix.searcher()
    mparser = MultifieldParser(["content", "title"], schema=ix.schema)

    query_raw = request.args.get('q', '')
    query = mparser.parse(unicode(query_raw.lower()))
    results = searcher.search(query)

    result_id = []
    for result in results:
        result_id.append(int(result['id']))

    result_id = list(set(result_id))
    wq = None
    for rid in result_id:
        if not wq:
            wq = Q(id=rid)
        else:
            wq |= Q(id=rid)
    if wq:
        coms = Commodity.select().where(wq)
    else:
        coms = []
    return render_template('core/com_list.html', commodities=coms)


# the account operations
@core.route('/account')
def account():
    kwargs = {
        'user':   g.user,
    }
    if request.args.get("login", None):
        kwargs['login'] = True
    if request.args.get("register", None):
        kwargs['register'] = True
    return render_template('core/account.html', **kwargs)


@core.route('/login', methods=['GET', 'POST'])
def login():
    post = request.json
    username = post.get("username", None)
    password = post.get("password", None)
    user = User.select().filter(username=username).execute().first()
    if user:
        if user.check_password(password):
            session['logged_in'] = True
            session['user_pk'] = user.get_pk()
            session.permanent = True
            g.user = user
            return jsonify(success=True, is_admin=user.admin)
        else:
            return jsonify(success=False, msg="Wrong Password")
    else:
        return jsonify(success=False, msg="No such user")


@core.route('/login/page', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('core/login.html', login=True,
                                next=request.args.get('next', None))
    else:
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        next_url = request.form.get("next", None)
        user = User.select().filter(username=username).execute().first()
        if user:
            if user.check_password(password):
                session['logged_in'] = True
                session['user_pk'] = user.get_pk()
                session.permanent = True
                g.user = user
                if next_url:
                    return redirect(next_url)
                return redirect(url_for('core.index'))
            else:
                return render_template('core/login.html',
                        login=True, error='Password error')
        else:
            return render_template('core/login.html',
                    login=True, error='No such user')


@core.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    session.pop('logged_in', None)
    g.user = None
    return redirect(url_for('core.index'))


@core.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('core/register.html', register=True)
    else:
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        passwordr = request.form.get('passwordr', None)
        if not username or not password or not passwordr:
            return render_template('core/register.html',
                    register=True, error='Can not be empty')
        if password != passwordr:
            return render_template('core/register.html',
                    register=True, error='Password Not The Same')
        if User.select().filter(username=username).exists():
            return render_template('core/register.html',
                    register=True, error='User has exist')
        user = User.create(username=username, password=password)
        #user.set_password(password)
        #user.save()
        session['logged_in'] = True
        session['user_pk'] = user.get_pk()
        session.permanent = True
        g.user = user
        return redirect(url_for('core.index'))
