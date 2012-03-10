from flask import Blueprint, render_template, g, session, jsonify, request
from util.auth import login_required 

member = Blueprint('member', __name__)

@member.route('/')
@login_required
def index():
    return render_template('member/index.html', member_center=True, user=g.user) 

@member.route('/account')
@login_required
def account():
    return render_template('member/stuff.html', user=g.user)

@member.route('/orders')
@login_required
def orders():
    return render_template('member/orders.html', user=g.user)

