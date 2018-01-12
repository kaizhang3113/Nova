# RESTful Server
# Copyright (c) 2016
#

import os
import sqlite3
import datetime
from random import randint
from flask import Flask, request, redirect, url_for, g, flash, jsonify
from werkzeug.utils import secure_filename


app = Flask(__name__, static_url_path='')
DATABASE = './db/picgallery.db'
UPLOAD_FORDER = "./static/pics"
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'picgallery.db'),
    SECRET_KEY = 'development',
    USERNAME='admin',
    PASSWORD='default'
))
app.config['UPLOAD_FORDER'] = UPLOAD_FORDER

# app.config['ALLOWED_EXTENSIONS'] = set(['jpeg'])
# app.config['MAX_CONTENT_LENGTH'] = 500 * 1024
# For a given file, return whether it's an allowed type or not

#Helper functions for database access and data retrieve/put
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    # rv.row_factory = sqlite3.Row
    rv.row_factory = dict_factory
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(exception):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#Initialize DB with given script "schema.sql"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql' , mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
#from yourapplication import init_db
#init_db()
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def submit_db(insert, args=(), one=False):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(insert, args)
    db.commit()
    flash("DONE")
    id = cursor.lastrowid
    cursor.close()
    return id


# Routes
# RESTful API
@app.route('/', methods=['GET'])
def index():
    return 'hi'
    return app.send_static_file('index.html')

@app.route('/init', methods=['GET'])
def init():
    init_db();
    return "Init DB Success"

@app.route('/images', methods=['GET', 'POST'])
def imagesService():
    if(request.method=='GET'):
        return jsonify(query_db('select * from images', [], one=False))
    else:
        uploaded_files = request.files.getlist("file[]");
        for file in uploaded_files:
            print file
            print file.content_type
            file.save(os.path.join(app.config['UPLOAD_FORDER'],'tmp'));
            print "file save"
            size = os.stat(os.path.join(app.config['UPLOAD_FORDER'],'tmp')).st_size
            print size
            if file.content_type == "image/jpeg" and size>1024:
                filename = secure_filename(file.filename)
                mylist = []
                mylist.append(datetime.date.today())
                dd = str(mylist[0])
                username = request.form["username"]
                if len(username)<1:
                    username = "U_"+str(randint(0,1000))
                tag = request.form["tag"]
                if len(tag)<1:
                    username = "T_"+str(randint(0,1000))
                result = submit_db('insert into images (name, extention, username, tag, dd) values(?, ?, ?, ?, ?)', [filename, file.content_type, username, tag, dd], one=True)
                target = os.path.join(app.config['UPLOAD_FORDER'],str(result));
                if not os.path.exists(target):
                    os.makedirs(target)
                os.rename(os.path.join(app.config['UPLOAD_FORDER'],'tmp'), os.path.join(target,filename))
                return app.send_static_file('index.html')
            else:
                return app.send_static_file('index.html')


@app.route('/comments/<int:idimage>', methods=['GET'])
def commentsGet(idimage):
    return jsonify(query_db('select * from comments where idimage=?', [idimage], one=False))

@app.route('/comments', methods=['POST'])
def commentsPost():
    idimage = request.form['iid']
    content = request.form['content']
    username = request.form['username']
    result = submit_db('insert into comments (idimage, comments, username) values (?, ?, ?) ', [idimage, content, username], one=True)
    print idimage, content, username,result
    return jsonify("success")

@app.route('/recently', methods=['GET'])
def recently():
    return jsonify(query_db('select * from images order by id desc limit 10', [], one=False))

@app.route('/users', methods=['GET'])
def users():
    return jsonify(query_db('select username, count(*) as count from images group by username', [], one=False))

@app.route('/tags', methods=['GET'])
def tags():
    return jsonify(query_db('select tag, count(*) as count from images group by tag', [], one=False))

@app.route('/topusers', methods=['GET'])
def topusers():
    return jsonify(query_db('select username , count(*) as count from images group by username order by count desc limit 10', [], one=False))

@app.route('/toptags', methods=['GET'])
def toptags():
    return jsonify(query_db('select tag, count(*) as count from images group by tag order by count desc limit 10', [], one=False))

if __name__ == '__main__':
    app.run(threaded=True)
