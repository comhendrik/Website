import os
from pydoc import render_doc
import json

from flask import * 

import json

def create_app():
    # create and configure the app
    IMAGE_FOLDER = os.path.join('static', 'images')
    app = Flask(__name__, instance_relative_config=True, template_folder='templates', static_folder='static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
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
        return render_template("blog.html")

    @app.route('/portfolio.html')
    def direct_to_portfolio():
        f = open('data/portfolio.json')
        data = json.load(f)
        f.close()
        return render_template("portfolio.html", portfolio_data = data)




    

    #from . import db
    #db.init_app(app)

    return app