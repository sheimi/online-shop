from flask import Blueprint, render_template, g, session, jsonify, request,\
        redirect, url_for

core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template('core/index.html', index=True, user=g.user) 

@core.route('/account')
def account():
    kwargs = {
        'user'    :   g.user,
    }
    if request.args.get("login", None):
        kwargs['login'] = True
    if request.args.get("register", None):
        kwargs['register'] = True
    return render_template('core/account.html', **kwargs)


@core.route('/login', methods=['GET', 'POST'])
def login():
    from models import User 
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
            return jsonify(success=True)
        else:
            return jsonify(success=False, msg="Wrong Password")
    else:
        return jsonify(success=False, msg="No such user")
        
@core.route('/login/page', methods=['GET', 'POST'])
def login_page():
    from models import User 
    if request.method == 'GET':
        return render_template('core/login.html', login=True, next=request.args.get('next', None))
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
                return render_template('core/login.html', login=True, error='Password error')
        else:
            return render_template('core/login.html', login=True, error='No such user')


@core.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    session.pop('logged_in', None)
    g.user = None
    return redirect(url_for('core.index'))

@core.route('/register', methods=['GET', 'POST'])
def register():
    from models import User, db
    if request.method == 'GET':
        return render_template('core/register.html', register=True)
    else:
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        passwordr = request.form.get('passwordr', None)
        if not username or not password or not passwordr:
            return render_template('core/register.html', register=True, error='Can not be empty')
        if password != passwordr:
            return render_template('core/register.html', register=True, error='Password Not The Same')
        if User.select().filter(username=username).exists():
            return render_template('core/register.html', register=True, error='User has exist')
        user = User.create(username=username, password=password)
        #user.set_password(password)
        #user.save()
        session["user_id"] = user.id
        return redirect(url_for('core.index')) 

