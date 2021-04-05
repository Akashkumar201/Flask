
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions
from datetime import datetime


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db=SQLAlchemy(app)
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)

    date= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author=db.Column(db.String(20),nullable=False,default="Annonymous")





    def __repr__(self):
        return 'Blog Post'+str(self.id)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/posts')
def post():
    return render_template('post.html',posts=all_posts)
if __name__=="__main__":
    app.run(debug=True)