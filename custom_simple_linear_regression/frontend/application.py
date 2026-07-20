from flask import Flask, render_template, request
from model import MyLr
import pandas as pd
import pickle
app = Flask(__name__)
model = pickle.load(open("customlr.pkl", "rb"))

@app.route('/')
def index():
       return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def calculateWeight():
       height = float(request.form.get('height'))
       print(height)
       result = model.predict(height)
       print(result)
       return str(result)  
if __name__ == "__main__":
    app.run(debug = True) 