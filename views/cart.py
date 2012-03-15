from flask import Blueprint, render_template, g, session, jsonify, request,\
        redirect, url_for
from models import *
from datetime import datetime as dt
from util.auth import login_required, get_object_or_404

cart = Blueprint('cart', __name__)

@cart.route('/cart-tool')
def cart_tool(): 
    if not g.user:
        return ""
    order = g.user.orders.where(is_confirmed=False).execute().first()
    if not order:
        order = UserOrder.create(user=g.user)
    g.user.cart = order
    num = order.items.count()
    return render_template('cart/tool.html', user=g.user, num=num)

@cart.route('/additem', methods=['POST'])
def additem():
    json = request.json
    order = get_object_or_404(UserOrder, id=json['order'])
    commodity = Commodity.select().get(id=json['commodity'])
    oi = OrderItem.create(commodity=commodity, order=order, num=json['num'], price=commodity.price)
    return jsonify(success=True)

@cart.route('/check/<int:order_id>')
def check_cart(order_id):
    order = get_object_or_404(UserOrder, id=order_id)
    if order.is_confirmed:
        #TODO
        return render_template('cart/success.html', user=g.user, order=order)
    return render_template('cart/check.html', user=g.user, order=order)

@cart.route('/check/<int:order_id>/address')
def check_address(order_id):
    order = get_object_or_404(UserOrder, id=order_id)
    if order.is_confirmed:
        #TODO
        return render_template('cart/success.html', user=g.user, order=order)
    return render_template('cart/address.html', user=g.user, order=order)

@cart.route('/check/<int:order_id>/payment')
def check_payment(order_id):
    order = get_object_or_404(UserOrder, id=order_id)
    if order.is_confirmed:
        #TODO
        return render_template('cart/success.html', user=g.user, order=order)
    return redirect(url_for('.confirm_order', order_id=order_id))

@cart.route('/confirm/<int:order_id>')
def confirm_order(order_id):
    order = get_object_or_404(UserOrder, id=order_id)
    if order.is_confirmed:
        #TODO
        return render_template('cart/success.html', user=g.user, order=order)
    return render_template('cart/confirm.html', user=g.user, order=order)

@cart.route('/confirm/<int:order_id>/all')
def confirm_all(order_id):
    order = get_object_or_404(UserOrder, id=order_id)
    UserOrder.update(is_confirmed=True, status=1, confirm_date=dt.today()).where(id=order_id).execute()
    return render_template('cart/success.html', user=g.user, order=order)

