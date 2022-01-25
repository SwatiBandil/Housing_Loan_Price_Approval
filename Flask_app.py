# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:09:47 2022

@author: pc
"""

from flask import Flask,request
from flasgger import Swagger
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
Swagger(app)

pickle_in=open("Logreg.pkl", "rb")
Logreg=pickle.load(pickle_in)

@app.route("/")
def Welcome():
    return "Welcome All"

@app.route('/predict', methods= ['Get'])
def predict_loan_Approval():
    
    """Let's Authenticate the Banks Loan Approval 
    This is using docstrings for specifications.
    ---
    parameters: 
      - name: Gender
        in: query
        type: string
        required: true
      - name: Married
        in: query
        type: string
      - name: Dependent
        in: query
        type: number
        required: true
      - name: Education
        in: query
        type: string
        required: true
      - name: ApplicantIncome
        in: query
        type: number
        required: true
      - name: Loan_Amount_Term
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    """
    
    Gender=request.args.get("Gender")
    Married=request.args.get("Marriesd")
    Dependent=request.args.get("Dependent")
    Education=request.args.get("Education")
    ApplicantIncome=request.args.get("ApplicantIncome")
    Loan_Amount_Term=request.args.get("Loan_Amount_Term")
    prediction=Logreg.predict([[Gender,Married,Dependent,Education,ApplicantIncome,Loan_Amount_Term]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_loan_file():
    """Let's Authenticate the Banks loans
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=Logreg.predict(df_test)
    
    return str(list(prediction))





if __name__== '__main__':
    app.run()