from unicodedata import category
from flask import Blueprint, render_template, request, redirect, url_for

import gridfs, codecs

bp = Blueprint('admin', __name__)

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["websiteDB"]

blog = db["blog"]

cv = db["cv"]

images_connection = client["images"]

FS = gridfs.GridFS(images_connection)

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

@bp.route('/create_cv_entry',methods=['GET','POST'])
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


@bp.route("/test-upload", methods=["GET","POST"])
def upload_image():
    if request.method == 'POST':
        # get current image file
        img_file = request.files['img']
        # get Content Type and File Name of current image
        content_type = img_file.content_type
        filename = img_file.filename
        # save to GridFS my image
        # fields <-- recive the id of just saved image
        fields = FS.put(img_file, content_type=content_type, filename=filename)
        print(fields)
        return "Succesfully inserted"
    return render_template("upload.html")

@bp.route("/test-image-query", methods=["GET"])
def image_query():
    images = images_connection["fs.files"]
    img_cursor = images.find()
    images_for_webpage = []
    for item in img_cursor:
        image = FS.get(item["_id"])
        base64_data = codecs.encode(image.read(), 'base64')
        image = base64_data.decode('utf-8')
        images_for_webpage.append(image)
    return render_template("images.html", images=images_for_webpage)