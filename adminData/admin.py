import os
from flask import flash, request, redirect, render_template, Blueprint, url_for
from werkzeug.utils import secure_filename


from Website.db import get_db, query_db

from Website.setup import YOURADMINNAME, YOURPASSWORD

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
        link = request.form.get('link')
        admin = request.form.get('admin')
        password = request.form.get('password')

        if admin != YOURADMINNAME or password != YOURPASSWORD:
            flash("Authentication failed")
            return redirect('create-blog-article')
        if not title or not body or not head or not icon or not r or not g or not b:
            flash("Problems at creation. You need to fill a fields. (The link field is optional)")
            return redirect('create-blog-article')
        
        db = get_db()
        cursor = db.cursor()
        try: 
            cursor.execute(f"INSERT INTO article (title, head, body, icon, r, g, b, link) VALUES ('{title}', '{head}', '{body}', '{icon}', '{r}', '{g}', '{b}', '{link}')")
            db.commit()
            db.close()

        except db.IntegrityError:
            flash("Problems with saving article to database")
            db.close()

        return redirect(url_for('direct_to_blog'))

        
    return render_template('admin/create.html')


@bp.route('/delete-blog-article',methods=['GET','POST'])
def delete_blog_article():
    if request.method == 'POST':
        id_of_article = request.form.get('idOfArticle')
        admin = request.form.get('admin')
        password = request.form.get('password')
        if admin != YOURADMINNAME or password != YOURPASSWORD:
            flash("Authentication failed")
            return redirect('delete-blog-article')
        db = get_db()
        cursor = db.cursor()
        try: 
            cursor.execute(f"DELETE FROM article WHERE id={id_of_article}")
            db.commit()
            db.close()

        except db.IntegrityError:
            flash("Problems with deleting article from database")
            db.close()
        
        flash(f"Article with id {id_of_article} has been deleted.")
        return redirect('delete-blog-article')
    db = get_db()
    cursor = db.cursor()
    results = query_db("SELECT * FROM article", cursor=cursor)
    results = sorted(results, key=lambda d: d['id'], reverse=True)
    db.close()
    return render_template("admin/delete.html", article=results)
    




