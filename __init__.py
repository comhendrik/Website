import os
import json

from flask import * 

from Website.db import get_db, query_db

import json

def create_app():
    # create and configure the app
    IMAGE_FOLDER = os.path.join('static', 'images')
    app = Flask(__name__, instance_relative_config=True, template_folder='templates', static_folder='static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
        UPLOAD_FOLDER = IMAGE_FOLDER
    )

    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/index')
    def direct_to_index():
        return render_template("index.html")

    @app.route('/about')
    def direct_to_about():
        return render_template("about.html")

    @app.route('/cv')
    def direct_to_cv():
        f = open('data/cv.json')
        data = json.load(f)
        f.close()
        return render_template("cv.html", cv_data = data)

    @app.route('/blog')
    def direct_to_blog():
        db = get_db()
        cursor = db.cursor()
        results = query_db("SELECT * FROM article", cursor=cursor)
        results = sorted(results, key=lambda d: d['id'], reverse=True)
        db.close()
        return render_template("blog.html", article=results)

    @app.route('/portfolio')
    def direct_to_portfolio():
        f = open('data/portfolio.json')
        data = json.load(f)
        f.close()
        return render_template("portfolio.html", portfolio_data = data)

    @app.route('/<int:article_id>')
    def direct_to_blog_article(article_id):
        db = get_db()
        cursor = db.cursor()
        results = query_db(f"SELECT * FROM article WHERE id={article_id}", cursor=cursor)
        db.close()
        if len(results) == 0:
            return render_template("404.html")
        return render_template("article.html", article=results[0])





    

    from . import db
    db.init_app(app)


    from Website.adminData import admin

    app.register_blueprint(admin.bp)

    return app