import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle

# app
app = Flask(__name__)
model = pickle.load(open('/Users/lindsayleedham/dsi10/projects/project_6/flask/model.pkl','rb'))

# routes
@app.route("/index", methods = ["GET","POST"])

def index():
   return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
