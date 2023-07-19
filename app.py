from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

# Load the trained model

model = joblib.load('Diabetes.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve the input data from the form
        pregnancies = int(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes_pedigree'])
        age = int(request.form['age'])

        # Perform necessary computations or model predictions
        input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
        prediction = model.predict(input_data)

        # Return the prediction result to the user
        if prediction[0] == 0:
            result = "The model predicts that the person does not have diabetes."
        else:
            result = "The model predicts that the person has diabetes."

        return render_template('result.html', result=result)

@app.route('/static/style.css')
def serve_css():
    return app.send_static_file('css/style.css')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model

model = joblib.load('Diabetes.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve the input data from the form
        pregnancies = int(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes_pedigree'])
        age = int(request.form['age'])

        # Perform necessary computations or model predictions
        input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]]
        prediction = model.predict(input_data)

        # Return the prediction result to the user
        if prediction[0] == 0:
            result = "The model predicts that the person does not have diabetes."
        else:
            result = "The model predicts that the person has diabetes."

        return render_template('result.html', result=result)

@app.route('/static/css/style.css')
def serve_css():
    return app.send_static_file('css/style.css')

if __name__ == '__main__':
    app.run(debug=True)
