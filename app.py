from typing import Tuple
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/Hello')
def hello():
    return "Hey Suno TO"
if __name__=="__main__":
    app.run(debug=True)