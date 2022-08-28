from flask import Blueprint, render_template, request, redirect, url_for, flash
import gridfs

import pymongo

from setup import websiteData

from bson.objectid import ObjectId

from bson import errors

delete_bp = Blueprint('delete', __name__)

@delete_bp.route('/blog',methods=['GET','POST'])
def delete_blog_entry():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        _id = request.form.get('_id')
        client = pymongo.MongoClient(authenticate(user, password))
        db = client["websiteDB"]
        blog = db["blog"]
        try:
            blog.delete_one({'_id': ObjectId(_id)})
        except errors.InvalidId:
           flash("incorrect id or no id")
           return render_template("delete_blog_entry.html", articles=blog.find(), websiteData=websiteData)
        except pymongo.errors.OperationFailure:
           flash("Authentication failed")
           return render_template("delete_blog_entry.html", articles=blog.find(), websiteData=websiteData)
        return redirect(url_for('direct_to_blog'))
    client = pymongo.MongoClient(websiteData["MONGODBCONNECTION"])
    db = client["websiteDB"]
    blog = db["blog"]
    return render_template("delete_blog_entry.html", articles=blog.find(), websiteData=websiteData)

@delete_bp.route('/cv',methods=['GET','POST'])
def delete_cv_entry():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        _id = request.form.get('_id')
        client = pymongo.MongoClient(authenticate(user, password))
        db = client["websiteDB"]
        cv = db["cv"]
        try:
            cv.delete_one({'_id': ObjectId(_id)})
        except errors.InvalidId:
           flash("incorrect id or no id")
           return render_template("delete_cv_entry.html", articles=cv.find(), websiteData=websiteData)
        except pymongo.errors.OperationFailure:
           flash("Authentication failed")
           return render_template("delete_cv_entry.html", articles=cv.find(), websiteData=websiteData)
        return redirect(url_for('direct_to_cv'))
    client = pymongo.MongoClient(websiteData["MONGODBCONNECTION"])
    db = client["websiteDB"]
    cv = db["cv"]
    return render_template("delete_cv_entry.html", articles=cv.find(), websiteData=websiteData)


@delete_bp.route('/portfolio',methods=['GET','POST'])
def delete_portfolio_entry():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        _id = request.form.get('_id')
        client = pymongo.MongoClient(authenticate(user, password))
        db = client["websiteDB"]
        portfolio = db["portfolio"]
        images_db = client["images"]
        fs = gridfs.GridFS(images_db)
        try:
            entry = portfolio.find_one({'_id': ObjectId(_id)})
            portfolio.delete_one({'_id': ObjectId(_id)})
            for image_id in entry['images']:
                fs.delete(image_id)
        except errors.InvalidId:
           flash("incorrect id or no id")
           return render_template("delete_portfolio_entry.html", articles=portfolio.find(), websiteData=websiteData)
        except pymongo.errors.OperationFailure:
           flash("Authentication failed")
           return render_template("delete_portfolio_entry.html", articles=portfolio.find(), websiteData=websiteData)
        return redirect(url_for('direct_to_portfolio'))
    client = pymongo.MongoClient(websiteData["MONGODBCONNECTION"])
    db = client["websiteDB"]
    portfolio = db["portfolio"]
    return render_template("delete_portfolio_entry.html", articles=portfolio.find(), websiteData=websiteData)

def authenticate(user, pwd):
    return f"mongodb://{user}:{pwd}@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin"