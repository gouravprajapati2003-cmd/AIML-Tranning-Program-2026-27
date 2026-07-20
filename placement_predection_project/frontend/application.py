from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("placementpred.pkl", "rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def doPredict():

    cgpa = float(request.form.get('cgpa'))
    iq = float(request.form.get('iq'))

    result = model.predict([[cgpa, iq]])

    if result[0] == 0:
        return "Placement will not be Done"
    else:
        return "Placement will be Done"

if __name__ == "__main__":
    app.run(debug=True)