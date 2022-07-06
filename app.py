import os
import json

from flask import * 

import json

from setup import websiteData

from Language import german, english

# create and configure the app
IMAGE_FOLDER = os.path.join('static', 'images')
application = Flask(__name__, instance_relative_config=True, template_folder='templates', static_folder='static')
application.config.from_mapping(
    SECRET_KEY='dev',
    UPLOAD_FOLDER = IMAGE_FOLDER
)

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
    f = open('data/cv.json')
    data = json.load(f)
    f.close()
    return render_template("cv.html", cv_data = data, websiteData=websiteData, text=TEXT.cv)

@application.route('/blog')
def direct_to_blog():
    f = open('data/blog.json')
    data = json.load(f)
    f.close()
    return render_template("blog.html", article=data, websiteData=websiteData, text=TEXT.blog)

@application.route('/portfolio')
def direct_to_portfolio():
    f = open('data/portfolio.json')
    data = json.load(f)
    f.close()
    return render_template("portfolio.html", portfolio_data = data, websiteData=websiteData, text=TEXT.portfolio)

@application.route('/<int:article_id>')
def direct_to_blog_article(article_id):
    f = open('data/blog.json')
    data = json.load(f)
    f.close()
    output_dict = [x for x in data if x['id'] == article_id]
    if len(output_dict) == 0:
        return render_template("404.html")
    return render_template("article.html", article=output_dict[0], websiteData=websiteData, text=TEXT.article)
