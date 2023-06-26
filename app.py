from flask import Flask,request,render_template
import numpy as np
import os
import pickle
# import config
# from Credit_API.utils import CreditCardApproval
model = pickle.load(open("Dtclf_model.pkl","rb"))

app = Flask(__name__)
@app.route('/')
def man():
    return render_template("index.html")
    # return "Hello mi"
@app.route("/Predict",methods =["POST"])
def index():
    data =request.form
    # print("user input data is",data)

    ID=int(data["ID"])
    CODE_GENDER=data["CODE_GENDER"]
    FLAG_OWN_CAR =data["FLAG_OWN_CAR"]
    FLAG_OWN_REALTY =data["FLAG_OWN_REALTY"]
    CNT_CHILDREN = int(data["CNT_CHILDREN"])
    AMT_INCOME_TOTAL =float(data["AMT_INCOME_TOTAL"])
    NAME_INCOME_TYPE =data["NAME_INCOME_TYPE"]
    NAME_EDUCATION_TYPE =data["NAME_EDUCATION_TYPE"]
    NAME_FAMILY_STATUS =data["NAME_FAMILY_STATUS"]
    NAME_HOUSING_TYPE =data["NAME_HOUSING_TYPE"]
    DAYS_BIRTH =int(data["DAYS_BIRTH"])
    DAYS_EMPLOYED =int(data["DAYS_EMPLOYED"])
    FLAG_MOBIL =int(data["FLAG_MOBIL"])
    FLAG_WORK_PHONE =int(data["FLAG_WORK_PHONE"])
    FLAG_PHONE =int(data["FLAG_PHONE"])
    FLAG_EMAIL =int(data["FLAG_EMAIL"])
    OCCUPATION_TYPE =data("OCCUPATION_TYPE")
    CNT_FAM_MEMBERS =float(data["CNT_FAM_MEMBERS"])
    array=np.array([[ID, CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, CNT_CHILDREN,
       AMT_INCOME_TOTAL, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE,
       NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, DAYS_BIRTH,
       DAYS_EMPLOYED, FLAG_MOBIL, FLAG_WORK_PHONE, FLAG_PHONE,
       FLAG_EMAIL, OCCUPATION_TYPE, CNT_FAM_MEMBERS]])
    result=model.Predict(array)
    
    return render_template('after.html',result=result)


if __name__ =="__main__":
    # app.debug = True
    # app.run()
    app.run()
    # host = 'localhost', port = 8088, debug = True

    # host='0.0.0.0', port=8080, debug=False 