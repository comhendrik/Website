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

    @app.route('/index.html')
    def direct_to_index():
        return render_template("index.html")

    @app.route('/cv.html')
    def direct_to_cv():
        f = open('data/cv.json')
        data = json.load(f)
        f.close()
        return render_template("cv.html", cv_data = data)

    @app.route('/blog.html')
    def direct_to_blog():
        db = get_db()
        cursor = db.cursor()
        results = query_db("SELECT * FROM article", cursor=cursor)
        results = sorted(results, key=lambda d: d['id'], reverse=True)
        return render_template("blog.html", article=results)

    @app.route('/portfolio.html')
    def direct_to_portfolio():
        f = open('data/portfolio.json')
        data = json.load(f)
        f.close()
        return render_template("portfolio.html", portfolio_data = data)




    

    from . import db
    db.init_app(app)


    from Website.adminData import admin

    app.register_blueprint(admin.bp)

    return app