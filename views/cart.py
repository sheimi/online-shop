from flask import Blueprint, render_template, g, jsonify, request,\
        redirect, url_for
from models.order import UserOrder, OrderItem, OrderStatus
from models.core import User
from models.commodity import Commodity
from datetime import datetime as dt
from util.auth import get_object_or_404

cart = Blueprint('cart', __name__)


@cart.route('/cart-tool')
def cart_tool():
    if not g.user:
        return ""
    order = g.user.orders.where(is_confirmed=False).execute().first()
    if not order:
        order = UserOrder.create(user=g.user,
                                 discount=g.user.check_membership().discount)
    g.user.cart = order
    num = order.items.count()
    return render_template('cart/tool.html', user=g.user, num=num)


@cart.route('/additem', methods=['POST'])
def additem():
    json = request.json
    order = get_object_or_404(UserOrder, id=json['order'])
    commodity = Commodity.select().get(id=json['commodity'])
    OrderItem.create(commodity=commodity, order=order, num=json['num'],
                     price=commodity.price)
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
    status = get_object_or_404(OrderStatus, name="confirmed")
    UserOrder.update(is_confirmed=True, status=status,
                     confirm_date=dt.today()).where(id=order_id).execute()
    point = g.user.point
    point += order.total_price()
    User.update(point=point).where(id=g.user.id).execute()
    return render_template('cart/success.html', user=g.user, order=order)
