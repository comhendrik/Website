from datetime import date
import os
import json

from flask import * 

from bson.objectid import ObjectId

import pymongo

import json

from setup import websiteData

from Language import german, english

import gridfs, codecs

# create and configure the app
IMAGE_FOLDER = os.path.join('static', 'images')
application = Flask(__name__, instance_relative_config=True, template_folder='templates', static_folder='static')
application.config.from_mapping(
    SECRET_KEY='dev',
    UPLOAD_FOLDER = IMAGE_FOLDER
)
client = pymongo.MongoClient(websiteData["MONGODBCONNECTION"])

db = client["websiteDB"]

blog = db["blog"]
cv = db["cv"]
portfolio = db["portfolio"]

images_connection = client["images"]

FS = gridfs.GridFS(images_connection)

#change language for your website
TEXT = german

@application.route('/index')
def direct_to_index():
    return render_template("index.html", websiteData=websiteData, text=TEXT.index)

@application.route('/about')
def direct_to_about():
    return render_template("about.html", websiteData=websiteData, text=TEXT.about)

@application.route('/cv')
def direct_to_cv():
    return render_template("cv.html", cv_data = cv.find(), websiteData=websiteData, text=TEXT.cv)

@application.route('/blog')
def direct_to_blog():
    return render_template("blog.html", article=blog.find(), websiteData=websiteData, text=TEXT.blog)

@application.route('/portfolio')
def direct_to_portfolio():
    data = []
    projects = portfolio.find()
    for project in projects:
        object = {
            "title" : project["title"],
            "description" : project["description"],
            "github_link" : project["github_link"],
            "images" : []
        }
        for img in project["images"]:
            image = FS.get(img)
            base64_data = codecs.encode(image.read(), 'base64')
            image = base64_data.decode('utf-8')
            object["images"].append(image)
        data.append(object)
    return render_template("portfolio.html", portfolio_data = data, websiteData=websiteData, text=TEXT.portfolio)

@application.route('/blog/<string:_id>')
def direct_to_blog_article(_id):
    data = blog.find({'_id': ObjectId(_id)}).limit(1)
    entry = list(data)
    if len(entry) == 0:
        return render_template("404.html")
    return render_template("article.html", article=entry[0], websiteData=websiteData, text=TEXT.article)

from admin import bp
application.register_blueprint(bp, url_prefix="/admin")