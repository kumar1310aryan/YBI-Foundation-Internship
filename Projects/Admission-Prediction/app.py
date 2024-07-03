from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd
import os


application = Flask(__name__)
app=application

model = pickle.load(open("models/model.pkl","rb"))

## Route for homepage

@app.route('/')
def index():
    return render_template('index.html')

## Route for Single data point prediction
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        #'GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA','Research'

        GRE_Score=int(request.form.get("GRE_Score"))
        TOEFL_Score= float(request.form.get('TOEFL_Score'))
        University_Rating = float(request.form.get('University_Rating'))
        SOP = float(request.form.get('SOP'))
        LOR = float(request.form.get('LOR'))
        BMI = float(request.form.get('BMI'))
        CGPA = float(request.form.get('CGPA'))
        Research = float(request.form.get('Research'))

        new_data=[[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA,Research]]
        predict=model.predict(new_data)
       
        result=predict
            
        return render_template('home.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")