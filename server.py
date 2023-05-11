from flask import *

import numpy

import pandas as pd

from sklearn import naive_bayes
from sklearn.naive_bayes import GaussianNB


app=Flask(__name__)

  
#HEART ATTACK PREDICTION
@app.route('/heart')
def heartpage():
    return render_template("heart.html")
  
@app.route('/heartattack', methods=["POST"])
def prediction():
  AGE=eval(request.form.get("AGE"))
  GENDER=int(request.form.get("GENDER"))
  CHEST=int(request.form.get("CHEST"))
  BLOOD=eval(request.form.get("BLOOD"))
  CHOLESTROL=eval(request.form.get("CHOLESTROL"))
  SUGAR=int(request.form.get("SUGAR"))
  ECG=int(request.form.get("ECG"))
  RATE=eval(request.form.get("RATE"))
  
  csv="heart.csv"
  data=pd.read_csv(csv)
  data=data.values
  x=data[:,:8]
  y=data[:,-1]

  model=GaussianNB()
  model.fit(x,y)
  
  prediction=model.predict([[AGE,GENDER,CHEST,BLOOD,CHOLESTROL,SUGAR,ECG,RATE]])
  
  return render_template("heart.html",data=prediction[0])


if __name__ == '__main__':
  app.run()