from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("Height.pkl", "rb"));

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def calculateWeight():
    height = float(request.form.get('height'))

    result = model.predict([[height]])

    weight = result.item()   

    return str(round(weight, 2))

if __name__ == "__main__":
    app.run(debug = True) 