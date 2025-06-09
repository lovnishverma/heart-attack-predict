
# 🫀 Heart Attack Prediction using Flask & Naive Bayes

This is a simple Flask-based web application that predicts the likelihood of a heart attack based on user inputs. It uses the **Gaussian Naive Bayes** algorithm from `scikit-learn` and a CSV dataset (`heart.csv`) for training.

## 🚀 Demo

![image](https://github.com/user-attachments/assets/6ae15aef-557c-4da5-bc3d-1b781d99121d)


![image](https://github.com/user-attachments/assets/f7724c45-3606-4007-beaf-17276a1081ee)


## 🧠 Machine Learning Model

- **Algorithm**: Gaussian Naive Bayes (`GaussianNB`)
- **Library**: `scikit-learn`
- **Input Features**:
  - AGE
  - GENDER (0 = Female, 1 = Male)
  - CHEST Pain Type
  - BLOOD Pressure
  - CHOLESTROL
  - SUGAR (0 = False, 1 = True)
  - ECG Results
  - RATE (Maximum Heart Rate)

## 📁 Project Structure

```plaintext
.
├── app.py              # Flask application
├── heart.csv           # Dataset for training
├── templates/
│   └── heart.html      # Frontend form and result display
└── README.md           # Project documentation
````

## 💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/heart-attack-prediction.git
cd heart-attack-prediction
```

### 2. Install Dependencies

Make sure you have Python 3.x installed.

```bash
pip install flask pandas scikit-learn
```

### 3. Run the Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 📝 Dataset

The `heart.csv` file should be in the following format (example):

| AGE | GENDER | CHEST | BLOOD | CHOLESTROL | SUGAR | ECG | RATE | TARGET |
| --- | ------ | ----- | ----- | ---------- | ----- | --- | ---- | ------ |
| 63  | 1      | 3     | 145   | 233        | 1     | 0   | 150  | 1      |
| ... | ...    | ...   | ...   | ...        | ...   | ... | ...  | ...    |

> The last column `TARGET` indicates whether a person had a heart attack (1 = Yes, 0 = No).

## 🛠 Technologies Used

* Python
* Flask
* Pandas
* scikit-learn (GaussianNB)
* HTML (Jinja2 templates)

## 📌 Notes

* Model is trained on-the-fly every time a prediction is made. For production, consider saving a trained model using `joblib` or `pickle`.
* No data normalization/scaling is done; depending on dataset quality, preprocessing might be required.

## 📷 UI Preview

```html
<!-- Sample form in heart.html -->
<form method="post" action="/heartattack">
  AGE: <input type="number" name="AGE"><br>
  GENDER: <select name="GENDER"><option value="0">Female</option><option value="1">Male</option></select><br>
  CHEST PAIN TYPE: <input type="number" name="CHEST"><br>
  BLOOD PRESSURE: <input type="number" name="BLOOD"><br>
  CHOLESTROL: <input type="number" name="CHOLESTROL"><br>
  SUGAR: <select name="SUGAR"><option value="0">No</option><option value="1">Yes</option></select><br>
  ECG: <input type="number" name="ECG"><br>
  HEART RATE: <input type="number" name="RATE"><br>
  <button type="submit">Predict</button>
</form>
```

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to fork the repo, submit PRs, and improve this application. Happy coding!

```

---

