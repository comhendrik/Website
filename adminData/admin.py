import os
from flask import flash, request, redirect, render_template, Blueprint
from werkzeug.utils import secure_filename


from Website.db import get_db, query_db

bp = Blueprint("bp_admin",__name__, url_prefix="/admin")

@bp.route('/create-blog-article',methods=['GET','POST'])
def create_blog_article():
    if request.method == 'POST':
        title = request.form.get('title')
        head = request.form.get('head')
        body = request.form.get('body')    
        icon = request.form.get('icon')
        r = request.form.get('r')
        g = request.form.get('g')
        b = request.form.get('b')    
        admin = request.form.get('admin')
        password = request.form.get('password')

        if admin != 'admin' or password != 'password':
            flash("Authentication failed")
            return redirect('create-blog-article')
        if not title or not body:
            flash("problems at creation")
            return redirect('create-blog-article')
        
        db = get_db()
        cursor = db.cursor()
        try: 
            cursor.execute(f"INSERT INTO article (title, head, body, icon, r, g, b) VALUES ('{title}', '{head}', '{body}', '{icon}', '{r}', '{g}', '{b}')")
            db.commit()
            db.close()

        except db.IntegrityError:
            flash("Problem with uploading post")
            db.close()

        return redirect('create-blog-article')

        
    return render_template('admin/create.html')


