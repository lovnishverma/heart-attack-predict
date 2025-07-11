from flask import Flask, render_template, request
import pandas as pd
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)

# Load and train model ONCE during app startup
data = pd.read_csv("heart.csv")
x = data.iloc[:, :8].values
y = data.iloc[:, -1].values
model = GaussianNB()
model.fit(x, y)

@app.route('/')
def heartpage():
    return render_template("heart.html")

@app.route('/heartattack', methods=["POST"])
def prediction():
    try:
        AGE = float(request.form.get("AGE"))
        GENDER = int(request.form.get("GENDER"))
        CHEST = int(request.form.get("CHEST"))
        BLOOD = float(request.form.get("BLOOD"))
        CHOLESTROL = float(request.form.get("CHOLESTROL"))
        SUGAR = int(request.form.get("SUGAR"))
        ECG = int(request.form.get("ECG"))
        RATE = float(request.form.get("RATE"))

        result = model.predict([[AGE, GENDER, CHEST, BLOOD, CHOLESTROL, SUGAR, ECG, RATE]])
        return render_template("heart.html", data=result[0])
    except Exception as e:
        return render_template("heart.html", error=f"Error: {e}")
