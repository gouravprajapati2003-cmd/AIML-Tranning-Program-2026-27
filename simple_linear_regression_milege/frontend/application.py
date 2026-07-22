from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("Milage.pkl", "rb"));

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def calculateMiles():
    Weight = float(request.form.get('Weight'))

    result = model.predict([[Weight]])

    Miles = result.item()   

    return str(round(Miles, 2))

if __name__ == "__main__":
    app.run(debug = True) 