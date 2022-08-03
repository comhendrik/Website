from unicodedata import category
from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('admin', __name__)

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["websiteDB"]

blog = db["blog"]

@bp.route('/create_blog_entry',methods=['GET','POST'])
def create_blog_entry():
    if request.method == 'POST':
        title = request.form.get('title')
        head = request.form.get('head') 
        body = request.form.get('body') 
        icon = request.form.get('icon') 
        link = request.form.get('link') 
        blog.insert_one({
            "title": f"{title}",
            "head": f"{head}",
            "body": f"{body}",
            "icon": f"{icon}",
            "link": f"{link}",
            "r": 0,
            "g": 0,
            "b": 0
        })
        return redirect(url_for('direct_to_blog'))
    return render_template("create_blog_entry.html")