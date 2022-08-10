from unicodedata import category
from flask import Blueprint, render_template, request, redirect, url_for

from app import FS

bp = Blueprint('admin', __name__)

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["websiteDB"]

blog = db["blog"]

cv = db["cv"]

portfolio = db["portfolio"]

@bp.route('/blog',methods=['GET','POST'])
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

@bp.route('/cv',methods=['GET','POST'])
def create_cv_entry():
    if request.method == 'POST':
        category = request.form.get('category')
        date = request.form.get('date') 
        description = request.form.get('description') 
        icon = request.form.get('icon')
        cv.insert_one({
            "category": f"{category}",
            "date": f"{date}",
            "description": f"{description}",
            "icon": f"{icon}"
        })
        return redirect(url_for('direct_to_cv'))
    return render_template("create_cv_entry.html")


@bp.route("/portfolio", methods=["GET","POST"])
def create_portfolio_entry():
    if request.method == 'POST':
        # get current image file
        title = request.form.get('title')
        description = request.form.get('description')
        github_link = request.form.get('github_link')
        img_list = request.files.getlist("img")
        images = []
        for img_file in img_list:
            # get Content Type and File Name of current image
            content_type = img_file.content_type
            filename = img_file.filename
            # save to GridFS my image
            # fields <-- recive the id of just saved image
            fields = FS.put(img_file, content_type=content_type, filename=filename)
            images.append(fields)
        
        portfolio.insert_one({
            "title": f"{title}",
            "description": f"{description}",
            "github_link": f"{github_link}",
            "images" : images
        })

        return redirect(url_for("direct_to_portfolio"))
    return render_template("create_portfolio_entry.html")