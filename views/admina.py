from flask import Blueprint, render_template, g, session, jsonify, request,\
        redirect, url_for
from util.auth import admin_required 
from models import *
from util.auth import get_object_or_404 

admina = Blueprint('admina', __name__)

@admina.route('/orders')
@admin_required
def orders():
    status_all = OrderStatus.select()
    return render_template('admin/admina/orders.html', status_all=status_all, order_page=True) 

@admina.route('/orders-list')
@admin_required
def orders_list():
    orders = UserOrder.select().filter(**request.args)
    return render_template('admin/admina/orders_list.html', orders = orders)

@admina.route('/categories')
@admin_required
def categories():
    root = get_object_or_404(Category, id=1)
    return render_template('admin/admina/categories.html', root=root)

@admina.route('/commodity-list')
@admin_required
def commodity_list():
    commodities = Commodity.select().filter(**request.args)
    return render_template('admin/admina/commodity_list.html', commodities=commodities)
