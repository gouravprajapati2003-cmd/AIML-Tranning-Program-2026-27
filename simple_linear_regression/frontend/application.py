from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("Placementpkg.pkl", "rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def doPredict():
    cgpa = float(request.form.get('cgpa'))

    result = model.predict([[cgpa]])

    return f"{result[0]:.2f} LPA"

if __name__ == "__main__":
    app.run(debug=True);