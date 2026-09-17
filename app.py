from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved Flask model
model_data = joblib.load("attrition_model.pkl")

# The notebook saved the model and Flask features
if isinstance(model_data, dict):
    model = model_data["model"]
    scaler = model_data["scaler"]
    flask_features = model_data["features"]
else:
    model = model_data
    scaler = None
    flask_features = [
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "JobSatisfaction"
    ]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":
        return render_template("predict.html")

    # Get values from the HTML form
    age = float(request.form["Age"])
    income = float(request.form["Income"])
    years = float(request.form["Years"])
    satisfaction = float(request.form["JobSatisfaction"])

    # Create input data
    sample = np.array([
        [age, income, years, satisfaction]
    ])

    # Apply scaling if scaler is available
    if scaler is not None:
        sample = scaler.transform(sample)

    # Make prediction
    prediction = model.predict(sample)[0]

    if prediction == 1:
        result = "Employee is likely to leave the company."
    else:
        result = "Employee is likely to stay in the company."

    return render_template(
        "result.html",
        prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)