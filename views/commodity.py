from flask import Blueprint, render_template, g, session, jsonify, request
from util.auth import login_required 
from models import *

commodity = Blueprint('commodity', __name__)

@commodity.route('/item/<int:item_id>')
def item(item_id):
    commodity = Commodity.select().get(id=item_id)
    commodity.img_name = commodity.imgs.execute().first().name
    return render_template('commodity/item.html', user=g.user, commodity=commodity)

@commodity.route('/item/<int:item_id>/comments')
def item_comments(item_id):
    commodity = Commodity.select().get(id=item_id)
    return render_template('commodity/item_comments.html', user=g.user, commodity=commodity)

@commodity.route('/comment/<int:comment_id>')
def comment(comment_id):
    comment = CommodityComment.select().get(id=comment_id)
    return render_template('commodity/item_comment.html', user=g.user, comment=comment)
