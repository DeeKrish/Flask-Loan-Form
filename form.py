from flask_wtf import Form
from wtforms import TextAreaField,IntegerField,RadioField,SubmitField,FloatField


class simpleform(Form):
    Gender = RadioField(label='Gender', choices=['Male','Female'])
    Married = RadioField(label='Married', choices=['Yes','No'])
    Dependents = IntegerField(label='Dependents',)
    Education = RadioField(label='Education', choices=['Graduate','Not'])
    self_employed = RadioField(label='self employed', choices=['Yes','No'])
    Applicantincome = FloatField(label='Applicant income')
    Coapplicantincome = FloatField(label='Co-applicant income',)
    Loanamount = FloatField(label='Loanamount',)
    Loan_amount_term = FloatField(label='Loan_amount_term',)
    Credit_History = RadioField(label='Credit_History', choices=['1','0'])
    Property_Area = RadioField(label='Property_Area', choices=['Urban','Rural','Semi Urban'])
    submit = SubmitField('Submit')
