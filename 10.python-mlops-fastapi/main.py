# Importing Dependencies
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import numpy as np
import pandas as pd
from prediction_model.config import config  
from prediction_model.processing.data_handling import load_pipeline,load_dataset



app = FastAPI()

model = load_pipeline(config.MODEL_NAME)


#Perform parsing
class LoanPred(BaseModel):
	Gender: str
	Married: str
	Dependents: str
	Education: str
	Self_Employed: str
	LoanAmount: float
	Loan_Amount_Term: float
	Credit_History: int
	Property_Area: str
	ApplicantIncome: float
	CoApplicant: float


@app.get('/')
def index():
    return {'message': 'Welcome to Loan Prediction App'}

# defining the function which will make the prediction using the data which the user inputs 
@app.post('/predict')
def predict_loan_status(loan_details: LoanPred):
	data = loan_details.model_dump()
	gender = data['Gender']
	married = data['Married']
	dependents = data['Dependents']
	education = data['Education']
	self_employed = data['Self_Employed']
	loan_amt = data['LoanAmount']
	loan_term = data['Loan_Amount_Term']
	credit_hist = data['Credit_History']
	property_area = data['Property_Area']
	applicant_income = data['ApplicantIncome']
	co_applicant = data["CoApplicant"]
    

	# Making predictions 
	print(pd.DataFrame([[gender, married, dependents, education, self_employed,applicant_income,co_applicant,loan_amt, loan_term, credit_hist, property_area]],columns=config.FEATURES))
	prediction = model.predict(pd.DataFrame([[gender, married, dependents, education, self_employed,applicant_income,co_applicant,loan_amt, loan_term, credit_hist, property_area]],columns=config.FEATURES))

	if prediction == 0:
		pred = 'Rejected'
	else:
		pred = 'Approved'

	return {'Status of Loan Application':pred}

if __name__ == '__main__':
	uvicorn.run(app, host='127.0.0.1', port=8080)