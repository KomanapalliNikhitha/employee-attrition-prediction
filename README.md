# Employee Attrition Prediction

## Project Overview

Employee Attrition Prediction is a Machine Learning and Data Analytics project that analyzes HR employee data and predicts employee attrition.

The project uses Python for data analysis and machine learning, Power BI for interactive data visualization, and Flask for a web-based prediction application.

## Objectives

- Analyze employee attrition patterns.
- Identify factors associated with employee turnover.
- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Build and evaluate machine learning classification models.
- Create an interactive Power BI dashboard.
- Develop a Flask web application for employee attrition prediction.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Power BI
- DAX
- Flask
- Jupyter Notebook

## Machine Learning

The project uses classification algorithms for employee attrition prediction, including:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Model performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

## Data Analysis

The project analyzes employee attributes such as:

- Age
- Job Role
- Department
- Monthly Income
- Overtime
- Job Satisfaction
- Work-Life Balance
- Years at Company
- Performance Rating

## Project Workflow

```text
Data Collection
       ↓
Data Cleaning
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Train-Test Split
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Attrition Prediction
       ↓
Power BI Dashboard
       ↓
Flask Web Application
```

## Repository Structure

```text
employee-attrition-prediction/
│
├── README.md
├── .gitignore
├── requirements.txt
├── app.py
├── Employee_Attrition.ipynb
├── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── attrition_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   ├── about.html
│   ├── index.html
│   ├── predict.html
│   └── result.html
│
└── docs/
    ├── Employee_Attrition.pptx
    ├── Execution_Script.txt
    ├── PowerBI_Dashboard_Guide.txt
    ├── Project_Report.docx
    └── Viva_Questions.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/KomanapalliNikhitha/employee-attrition-prediction.git
```

### 2. Go to the project folder

```bash
cd employee-attrition-prediction
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

## Run the Flask Application

Run:

```bash
python app.py
```

Then open the local Flask URL displayed in the terminal.

## Jupyter Notebook

Open `Employee_Attrition.ipynb` using Jupyter Notebook or JupyterLab to explore:

- Data cleaning
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training
- Model evaluation
- Employee attrition prediction

## Power BI Dashboard

The project includes documentation for creating the Power BI dashboard using the HR employee dataset.

Refer to:

```text
docs/PowerBI_Dashboard_Guide.txt
```

## Project Documentation

Additional project materials are available in the `docs/` folder:

- Project Report
- PowerPoint Presentation
- Power BI Dashboard Guide
- Viva Questions
- Execution Script

## Disclaimer

This project is developed for academic and learning purposes using the IBM HR Analytics Employee Attrition dataset.

Model performance and project claims should be based on the results obtained from the final executed notebook.
