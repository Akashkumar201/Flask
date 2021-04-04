from app import hello
from flask import Flask
from flask.helpers import flash

app = Flask(__name__)
@app.route('/home/user/<string:username>/posts/<int:id>')
def function(username,id):
    return "Hello,"+username+" You are watching your post which id: "+str(id)

@app.route('/onlyget',methods=['GET','POST'])
def get_req():
    return 'Hello All'

if __name__=="__main__":
    app.run(debug=True)