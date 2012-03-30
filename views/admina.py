from flask import Blueprint, render_template, jsonify, request
from util.auth import admin_required
from models.commodity import Category, Commodity, CommodityImage
from models.order import OrderStatus, UserOrder
from util.auth import get_object_or_404

admina = Blueprint('admina', __name__)


@admina.route('/orders')
@admin_required
def orders():
    status_all = OrderStatus.select()
    return render_template('admin/admina/orders.html', status_all=status_all,
                                                       order_page=True)


@admina.route('/orders-list')
@admin_required
def orders_list():
    orders = UserOrder.select().filter(**request.args)
    return render_template('admin/admina/orders_list.html', orders=orders)


@admina.route('/categories')
@admin_required
def categories():
    root = get_object_or_404(Category, id=1)
    return render_template('admin/admina/categories.html', root=root)


@admina.route('/commodity-list')
@admin_required
def commodity_list():
    commodities = Commodity.select().filter(**request.args)
    return render_template('admin/admina/commodity_list.html',
                            commodities=commodities)


@admina.route('/images/<int:com_id>')
@admin_required
def commodity_image(com_id):
    commodity = get_object_or_404(Commodity, id=com_id)
    return render_template('admin/admina/image_list.html', commodity=commodity)


@admina.route('/images/delete', methods=['DELETE'])
@admin_required
def image_delete():
    img = get_object_or_404(CommodityImage, id=request.json.get('id', None))
    img.delete_instance()
    path = "/".join(['./static/img/commodity', img.name])
    import os
    os.remove(path)
    return jsonify(success=True)


@admina.route('/images/upload/<int:com_id>', methods=['POST'])
@admin_required
def image_upload(com_id):
    datafile = request.files['file']
    filename = datafile.filename
    path = "/".join(['./static/img/commodity', filename])
    url = "/".join(['/static/img/commodity', filename])

    commodity = get_object_or_404(Commodity, id=com_id)
    img = CommodityImage.create(name=filename, commodity=commodity)

    datafile.save(path)
    return jsonify(success=True, url=url, img_id=img.id)
