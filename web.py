import joblib
from flask import Flask, request, redirect, url_for, render_template
import numpy as np
import pandas as pd
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')





@app.route('/predict')
def predict():
    number = request.args.get('number')
    return render_template('predict.html',number=number)




@app.route('/predict/load',methods=['GET'])
def load():
    age = request.args.get('age')
    gender = request.args.get('gender')
    department = request.args.get('department')
    title = request.args.get('title')
    experience = request.args.get('experience')
    education = request.args.get('education')
    location = request.args.get('location')

    loaded_model = joblib.load("salary_model.joblib")
    X = pd.DataFrame([{
        "Age": int(age),
        "Gender": gender,
        "Department": department,
        "Job_Title": title,
        "Experience_Years": int(experience),
        "Education_Level": education,
        "Location": location
    }])


    number = loaded_model.predict(X)[0]
    

    return redirect(url_for("predict",number=number))





if __name__ == '__main__':
    app.run(debug=True)
