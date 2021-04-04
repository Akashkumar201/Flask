from flask import Flask

app=Flask(__name__)

@app.route('/home/user/<string:username>/posts/<int:id>')
def function(username,id):
    return "Hello,"+username+" You are watching your post which id: "+str(id)
if __name__=="__main__":
    app.run(debug=True)