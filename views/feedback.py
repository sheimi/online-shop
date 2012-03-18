from flask import Blueprint, render_template, g, session, jsonify, request,\
        redirect, url_for
from models import *
from datetime import datetime as dt
from util.auth import login_required, get_object_or_404

feedback = Blueprint('feedback', __name__)

@feedback.route('/tool')
def tool(): 
    return render_template('feedback/tool.html')

@feedback.route('/box')
def box():
    return render_template('feedback/feed_box.html')

@feedback.route('/feeds')
def feeds():
    feed_list = Feedback.select()
    return render_template('feedback/list.html', feeds=feed_list)

@feedback.route('/feed/<int:feed_id>')
def feed(feed_id):
    feed_item = get_object_or_404(Feedback, id=feed_id)
    return render_template('feedback/feed_item.html', feed=feed_item)
