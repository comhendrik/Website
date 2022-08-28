from flask import Blueprint, render_template, request, redirect, url_for, flash

import gridfs

create_bp = Blueprint('create', __name__)

import pymongo

@create_bp.route('/blog',methods=['GET','POST'])
def create_blog_entry():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        client = pymongo.MongoClient(authenticate(user, password))
        db = client["websiteDB"]
        blog = db["blog"]
        title = request.form.get('title')
        head = request.form.get('head') 
        body = request.form.get('body') 
        icon = request.form.get('icon') 
        link = request.form.get('link')
        r = request.form.get('r') 
        g = request.form.get('g') 
        b = request.form.get('b')
        try:
            blog.insert_one({
            "title": f"{title}",
            "head": f"{head}",
            "body": f"{body}",
            "icon": f"{icon}",
            "link": f"{link}",
            "r": int(r),
            "g": int(g),
            "b": int(b)
            })
        except pymongo.errors.OperationFailure:
           flash("Authentication failed")
           return render_template("create_blog_entry.html")
        return redirect(url_for('direct_to_blog'))
    return render_template("create_blog_entry.html")

@create_bp.route('/cv',methods=['GET','POST'])
def create_cv_entry():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        client = pymongo.MongoClient(authenticate(user, password))
        db = client["websiteDB"]
        cv = db["cv"]
        category = request.form.get('category')
        date = request.form.get('date') 
        description = request.form.get('description') 
        icon = request.form.get('icon')
        
        try:
            cv.insert_one({
            "category": f"{category}",
            "date": f"{date}",
            "description": f"{description}",
            "icon": f"{icon}"
        })
        except pymongo.errors.OperationFailure:
           flash("Authentication failed")
           return render_template("create_cv_entry.html")
        return redirect(url_for('direct_to_cv'))
    return render_template("create_cv_entry.html")


@create_bp.route("/portfolio", methods=["GET","POST"])
def create_portfolio_entry():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        client = pymongo.MongoClient(authenticate(user, password))
        db = client["websiteDB"]
        portfolio = db["portfolio"]
        title = request.form.get('title')
        description = request.form.get('description')
        github_link = request.form.get('github_link')
        img_list = request.files.getlist("img")
        images = []
        images_connection = client["images"]

        FS = gridfs.GridFS(images_connection)
        try:
            for img_file in img_list:
                content_type = img_file.content_type
                filename = img_file.filename
                _id = FS.put(img_file, content_type=content_type, filename=filename)
                images.append(_id)
        
            portfolio.insert_one({
                "title": f"{title}",
                "description": f"{description}",
                "github_link": f"{github_link}",
                "images" : images
            })
        except pymongo.errors.OperationFailure:
            flash("Authentication failed")
            return render_template("create_portfolio_entry.html")
        
        return redirect(url_for("direct_to_portfolio"))
    return render_template("create_portfolio_entry.html")


def authenticate(user, pwd):
    return f"mongodb://{user}:{pwd}@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin"