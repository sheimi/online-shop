from flask import Blueprint, render_template, g, session, jsonify, request,\
        redirect, url_for
from models import *

cart = Blueprint('cart', __name__)

@cart.route('/cart-tool')
def cart_tool(): 
    if not g.user:
        return ""
    order = g.user.orders.where(is_complete=False).execute().first()
    if not order:
        order = UserOrder.create(user=g.user)
    g.user.cart = order
    num = order.items.count()
    return render_template('cart/tool.html', user=g.user, num=num)

@cart.route('/additem', methods=['POST'])
def additem():
    json = request.json
    order = UserOrder.select().get(id=json['order'])
    commodity = Commodity.select().get(id=json['commodity'])
    oi = OrderItem.create(commodity=commodity, order=order, num=json['num'], price=commodity.price)
    return jsonify(success=True)

@cart.route('/check/<int:order_id>')
def check_cart(order_id):
    order = UserOrder.select().get(id=order_id)
    return render_template('cart/check.html', user=g.user, order=order)

