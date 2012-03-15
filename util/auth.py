from functools import wraps
from flask import g, request, redirect, url_for, abort

def login_required(f):

    @wraps(f)
    def decoratored_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('core.login_page', next=request.url))
        return f(*args, **kwargs)
    
    return decoratored_function

def admin_required(f):

    @wraps(f)
    def decoratored_function(*args, **kwargs):
        if g.user and g.user.is_admin:
            return f(*args, **kwargs)
        return redirect(url_for('core.login_page', next=request.url))
    
    return decoratored_function

def get_object_or_404(model, **kwargs):
    try:
        return model.get(**kwargs)
    except model.DoesNotExist:
        abort(404)
