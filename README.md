# Employee Attrition Prediction using Machine Learning

A Machine Learning and Data Analytics project developed to analyze employee attrition patterns and predict whether an employee is likely to leave or stay in an organization.

The project uses HR employee data to perform data cleaning, preprocessing, exploratory data analysis (EDA), feature engineering, machine learning model training, model evaluation, prediction, and visualization.

A Flask web application is also developed to allow users to enter employee details and receive an attrition prediction.

---

## 📌 Project Overview

Employee attrition refers to employees leaving an organization voluntarily or involuntarily.

High employee attrition can affect an organization through:

- Increased recruitment costs
- Loss of experienced employees
- Increased workload for existing employees
- Reduced productivity
- Training and onboarding costs
- Loss of organizational knowledge

This project applies Machine Learning techniques to HR data to identify patterns associated with employee attrition.

The system analyzes employee-related attributes such as:

- Age
- Monthly Income
- Job Satisfaction
- Years at Company
- Overtime
- Job Role
- Department
- Work-Life Balance
- Performance Rating
- Gender
- Years of Experience
- Other HR-related attributes available in the dataset

The final system provides a prediction indicating whether an employee is likely to leave or stay.

---

# 🎯 Objectives

The main objectives of this project are:

1. Collect and understand HR employee data.
2. Perform data cleaning and preprocessing.
3. Analyze employee attrition using Exploratory Data Analysis.
4. Identify important factors associated with employee attrition.
5. Convert categorical data into numerical form for Machine Learning.
6. Split the dataset into training and testing datasets.
7. Train multiple Machine Learning classification models.
8. Compare model performance using evaluation metrics.
9. Develop an employee attrition prediction system.
10. Save the trained Machine Learning model.
11. Develop a Flask web application for prediction.
12. Provide HR-related insights using data visualization.
13. Prepare Power BI dashboard documentation for business analysis.

---

# 📊 Dataset

The project uses the IBM HR Analytics Employee Attrition dataset.

### Dataset File

```text
WA_Fn-UseC_-HR-Employee-Attrition.csv
```

The dataset contains employee-related information and an `Attrition` target variable.

### Target Variable

```text
Attrition
```

The target variable represents whether an employee has left the organization.

Example:

```text
Yes → Employee left
No  → Employee stayed
```

---

# 🔍 Important Dataset Attributes

Some important attributes analyzed in the project include:

| Attribute | Description |
|---|---|
| Age | Age of the employee |
| Gender | Gender of the employee |
| Department | Employee's department |
| JobRole | Job role of the employee |
| MonthlyIncome | Monthly salary/income |
| JobSatisfaction | Employee job satisfaction level |
| WorkLifeBalance | Work-life balance rating |
| YearsAtCompany | Number of years spent at the company |
| YearsInCurrentRole | Years in current role |
| PerformanceRating | Employee performance rating |
| OverTime | Whether the employee works overtime |
| BusinessTravel | Employee travel frequency |
| Attrition | Target variable indicating employee attrition |

---

# 🛠 Technologies Used

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy
- Statistical Analysis

## Data Visualization

- Matplotlib
- Seaborn
- Power BI
- DAX

## Machine Learning

- Scikit-learn
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

## Web Development

- Flask
- HTML
- CSS

## Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

## Model Saving

- Joblib

---

# 🔄 Project Workflow

The complete project workflow is:

```text
Data Collection
      ↓
Data Loading
      ↓
Data Understanding
      ↓
Data Cleaning
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Categorical Encoding
      ↓
Train/Test Split
      ↓
Feature Scaling
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Comparison
      ↓
Final Model Selection
      ↓
Model Saving
      ↓
Flask Application
      ↓
Employee Prediction
      ↓
Power BI Analysis
```

---

# 🧹 1. Data Cleaning

The first step is to inspect the dataset and identify potential data quality issues.

The project checks:

- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate records
- Unique values
- Basic statistical information

Example operations include:

```python
df.shape
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
```

Data cleaning ensures that the dataset is suitable for further analysis and Machine Learning.

---

# 🔧 2. Data Preprocessing

Machine Learning algorithms require numerical input.

The HR dataset contains both numerical and categorical attributes.

Examples of categorical attributes include:

```text
Gender
Department
JobRole
OverTime
BusinessTravel
Attrition
```

Categorical variables are converted into numerical representations before model training.

The project uses `LabelEncoder` for categorical encoding.

Example:

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df_ml[column] = encoder.fit_transform(df_ml[column].astype(str))
```

This allows Machine Learning algorithms to process the categorical information.

---

# 📈 3. Exploratory Data Analysis

Exploratory Data Analysis (EDA) is performed to understand the structure and patterns in the HR dataset.

The project analyzes relationships between employee attributes and attrition.

Visualizations include:

- Attrition distribution
- Attrition by gender
- Attrition by department
- Attrition by job role
- Attrition by overtime
- Attrition by job satisfaction
- Attrition by work-life balance
- Attrition by age
- Attrition by monthly income
- Attrition by years at company

Example visualization:

```python
sns.countplot(x="Attrition", data=df)
plt.title("Employee Attrition Distribution")
plt.show()
```

EDA helps identify patterns that may be useful for prediction and HR analysis.

---

# 🔗 4. Correlation Analysis

Correlation analysis is used to understand relationships between numerical variables.

A correlation heatmap is generated using numerical features.

Example:

```python
numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_df.corr(),
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()
```

The heatmap provides a visual representation of relationships between numerical attributes.

---

# ⚙️ 5. Feature Engineering

Feature engineering involves preparing and transforming the available features so that they can be effectively used by Machine Learning models.

The project prepares employee attributes for model training by:

- Encoding categorical variables
- Selecting input features
- Separating input variables from the target
- Scaling numerical values where required

The target variable is:

```text
Attrition
```

The remaining employee attributes are used as input features.

---

# ✂️ 6. Train/Test Split

The dataset is divided into two parts:

```text
Training Data → Used to train the model
Testing Data  → Used to evaluate the model
```

The project uses:

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Approximately 80% of the data is used for training and 20% for testing.

The test dataset is kept separate so that model performance can be evaluated on data that was not used during training.

---

# 📏 7. Feature Scaling

StandardScaler is used to standardize features where scaling is required.

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

The scaler learns the transformation from the training data and applies the same transformation to the testing data.

---

# 🤖 8. Machine Learning Models

Multiple classification algorithms are used in the project.

## Logistic Regression

Logistic Regression is a classification algorithm used to estimate the probability of a class.

It provides a simple baseline model for the classification problem.

---

## Decision Tree

A Decision Tree makes predictions using a sequence of decision rules.

It can be visualized as a tree structure:

```text
Root
 ↓
Decision
 ↓
Decision
 ↓
Prediction
```

Decision Trees are useful because their decision process can be relatively easy to interpret.

---

## Random Forest

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees.

Instead of depending on a single tree, Random Forest creates several trees and combines their predictions.

Conceptually:

```text
              Dataset
                 ↓
       ┌─────────┼─────────┐
       ↓         ↓         ↓
     Tree 1    Tree 2    Tree 3
       ↓         ↓         ↓
       └─────────┼─────────┘
                 ↓
          Final Prediction
```

The project uses Random Forest as one of the main classification models.

---

## XGBoost

XGBoost is a gradient boosting algorithm designed for classification and regression tasks.

It builds models sequentially, with later models focusing on improving errors made by earlier models.

XGBoost is included to compare its performance with other classification algorithms.

---

# 📊 9. Model Evaluation

The trained models are evaluated using several metrics.

The project uses:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

---

## Accuracy

Accuracy represents the proportion of total predictions that are correct.

```text
Accuracy =
Correct Predictions / Total Predictions
```

---

## Precision

Precision measures how many employees predicted as attrition cases were actually attrition cases.

```text
Precision =
True Positives / (True Positives + False Positives)
```

---

## Recall

Recall measures how many actual attrition cases were correctly identified by the model.

```text
Recall =
True Positives / (True Positives + False Negatives)
```

Recall can be particularly useful when identifying employees who actually leave is important.

---

## F1-Score

F1-score combines Precision and Recall into a single metric.

```text
F1 = 2 × (Precision × Recall)
     --------------------------
       Precision + Recall
```

---

## ROC-AUC

ROC-AUC measures the model's ability to distinguish between the two classes across classification thresholds.

A higher ROC-AUC generally indicates better class separation.

---

## Confusion Matrix

The confusion matrix shows:

```text
                 Predicted
                Stay  Leave

Actual Stay      TN     FP

Actual Leave     FN     TP
```

Where:

- TP = True Positive
- TN = True Negative
- FP = False Positive
- FN = False Negative

---

# 📋 10. Model Comparison

The project compares multiple Machine Learning models based on their evaluation metrics.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | Notebook Output | Notebook Output | Notebook Output | Notebook Output | Notebook Output |
| Decision Tree | Notebook Output | Notebook Output | Notebook Output | Notebook Output | Notebook Output |
| Random Forest | Notebook Output | Notebook Output | Notebook Output | Notebook Output | Notebook Output |
| XGBoost | Notebook Output | Notebook Output | Notebook Output | Notebook Output | Notebook Output |

The final metric values should always be taken from the latest executed notebook output.

---

# 🌲 11. Feature Importance

Feature importance can be used with tree-based models such as Random Forest to understand which features contribute to the model's predictions.

Example:

```python
importance = model.feature_importances_
```

A feature importance visualization can then be created to understand the relative contribution of different employee attributes.

This can help identify variables that are useful for further HR analysis.

---

# 💾 12. Model Saving

After training, the model is saved using Joblib.

Example:

```python
import joblib

joblib.dump(model_data, "attrition_model.pkl")
```

The saved model file is:

```text
attrition_model.pkl
```

The saved model and preprocessing information can then be loaded by the Flask application without retraining the model every time the application starts.

---

# 🌐 13. Flask Web Application

A Flask-based web application is developed to provide a simple interface for employee attrition prediction.

The application allows the user to enter:

- Age
- Monthly Income
- Years at Company
- Job Satisfaction

The entered information is processed and passed to the trained Machine Learning model.

The application then displays the prediction.

Example output:

```text
Employee is likely to stay in the company.
```

or:

```text
Employee is likely to leave the company.
```

The displayed result depends on the trained model and the entered employee information.

---

# 🖥️ Flask Application Flow

```text
User
 ↓
Open Flask Website
 ↓
Enter Employee Details
 ↓
Submit Form
 ↓
Flask Receives Input
 ↓
Input Preprocessing
 ↓
Feature Scaling
 ↓
Loaded ML Model
 ↓
Prediction
 ↓
Result Page
```

---

# 📁 Flask Application Structure

```text
app.py
│
├── Load trained model
│
├── Home route
│
├── About route
│
└── Prediction route
       ↓
   Receive user input
       ↓
   Preprocess input
       ↓
   Generate prediction
       ↓
   Display result
```

---

# 📊 14. Power BI Dashboard

Power BI is used as part of the analytics component of the project.

The dashboard can be used to analyze employee attrition patterns through interactive visualizations.

Potential dashboard analysis includes:

- Total Employees
- Attrition Count
- Attrition Rate
- Attrition by Department
- Attrition by Job Role
- Attrition by Gender
- Attrition by Age
- Attrition by Job Satisfaction
- Attrition by Work-Life Balance
- Attrition by Overtime
- Attrition by Monthly Income
- Attrition by Years at Company

DAX measures can be used to calculate HR metrics and support interactive analysis.

Detailed Power BI instructions are available in:

```text
docs/PowerBI_Dashboard_Guide.txt
```

---

# 📂 Repository Structure

```text
employee-attrition-prediction/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── app.py
├── Employee_Attrition.ipynb
├── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── attrition_model.pkl
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── predict.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── docs/
    ├── Project_Report.docx
    ├── Employee_Attrition.pptx
    ├── PowerBI_Dashboard_Guide.txt
    ├── Viva_Questions.txt
    └── Execution_Script.txt
```

---

# 📄 Project Files

### `Employee_Attrition.ipynb`

Contains the complete Machine Learning workflow:

- Data loading
- Data exploration
- Data cleaning
- Preprocessing
- EDA
- Feature engineering
- Model training
- Model evaluation
- Prediction
- Model saving

---

### `WA_Fn-UseC_-HR-Employee-Attrition.csv`

Contains the HR employee dataset used for analysis and Machine Learning.

---

### `attrition_model.pkl`

Contains the saved trained model and preprocessing information used by the Flask application.

---

### `app.py`

Main Flask application responsible for:

- Loading the model
- Receiving user input
- Processing employee information
- Generating predictions
- Displaying prediction results

---

### `templates/`

Contains HTML pages used by the Flask application:

```text
index.html
about.html
predict.html
result.html
```

---

### `static/style.css`

Contains the CSS styling used for the Flask web pages.

---

### `docs/`

Contains project-related documentation:

- Project Report
- Power BI Guide
- Presentation
- Viva Questions
- Execution Script

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/KomanapalliNikhitha/employee-attrition-prediction.git
```

Move into the project directory:

```bash
cd employee-attrition-prediction
```

---

## 2. Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

The project requires Python libraries including:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
flask
joblib
```

---

# 🚀 Run the Flask Application

From the project directory, run:

```bash
python app.py
```

The Flask development server will start.

Open the local URL displayed in the terminal, for example:

```text
http://127.0.0.1:5000
```

---

# 📓 Run the Jupyter Notebook

Open:

```text
Employee_Attrition.ipynb
```

using:

- Jupyter Notebook
- JupyterLab
- VS Code with the Jupyter extension

Run the notebook cells sequentially to review:

```text
Data Analysis
      ↓
Preprocessing
      ↓
EDA
      ↓
Machine Learning
      ↓
Evaluation
      ↓
Prediction
```

---

# 🧪 Example Prediction

The Flask application accepts employee details through a web form.

Example input:

```text
Age: 30
Monthly Income: 5000
Years at Company: 5
Job Satisfaction: 3
```

The model processes these values and produces a classification result.

Example:

```text
Employee is likely to stay in the company.
```

The displayed result depends on the trained model and the entered employee information.

---

# 📈 Project Outcomes

The project demonstrates how Machine Learning and Data Analytics can be applied to an HR-related classification problem.

The project provides practical experience in:

- Data preprocessing
- Exploratory Data Analysis
- Data visualization
- Feature engineering
- Classification algorithms
- Model evaluation
- Model comparison
- Model persistence
- Flask application development
- Power BI analytics
- Git and GitHub project management

---

# 💡 Key Learning Outcomes

Through this project, the following concepts were implemented.

## Python

- Variables
- Functions
- Libraries
- File handling
- Data processing

## Pandas & NumPy

- DataFrame operations
- Data selection
- Data transformation
- Numerical operations

## Data Analysis

- Data cleaning
- Missing-value analysis
- Duplicate detection
- Statistical analysis
- Exploratory Data Analysis

## Machine Learning

- Classification
- Train/Test Split
- Feature Encoding
- Feature Scaling
- Model Training
- Model Evaluation
- Prediction

## Visualization

- Matplotlib
- Seaborn
- Correlation Heatmaps
- Distribution plots
- Classification plots

## Web Development

- Flask
- HTML
- CSS
- Form handling
- Machine Learning model integration

## Business Intelligence

- Power BI
- DAX
- HR analytics
- Dashboard development

## Version Control

- Git
- GitHub
- Repository management
- Git commits
- Git push and pull

---

# ⚠️ Important Note About Model Metrics

Model performance metrics can change depending on:

- Dataset version
- Preprocessing approach
- Feature selection
- Train/test split
- Model parameters
- Random state
- Execution environment

Therefore, the accuracy, precision, recall, F1-score, and ROC-AUC reported in the repository should be taken from the **final executed notebook output**.

The project README intentionally does not claim a fixed model accuracy.

---

# 🔐 Disclaimer

This project is intended for:

- Educational purposes
- Academic demonstration
- Machine Learning practice
- Data Analytics learning

The predictions should not be used as the sole basis for real-world employment decisions.

Employee attrition prediction can involve sensitive workplace information, and real-world HR applications should include appropriate privacy, fairness, security, and human review considerations.

---

# 👩‍💻 Author

**Komanapalli Nikhitha**

B.Tech Information Technology

MVGR College of Engineering

---

# 🔗 Project Repository

GitHub:

https://github.com/KomanapalliNikhitha/employee-attrition-prediction

---

# ⭐ Future Enhancements

Possible future improvements include:

- Hyperparameter tuning
- Cross-validation
- Improved handling of class imbalance
- Advanced feature engineering
- Explainable AI techniques
- SHAP-based model explanations
- Improved Flask UI
- Cloud deployment
- Real-time Power BI integration
- User authentication
- Database integration
- Model monitoring

---

# 📌 Conclusion

The Employee Attrition Prediction project demonstrates a complete Machine Learning workflow starting from HR data analysis and preprocessing through model training, evaluation, prediction, and web application integration.

The project combines:

```text
Python
+
Data Analytics
+
Machine Learning
+
Data Visualization
+
Power BI
+
Flask
+
GitHub
```

to create an end-to-end academic Machine Learning and analytics project.

The system provides a practical demonstration of how employee data can be processed and analyzed to support attrition-related analysis and predictive modeling.
