# Customer-Churn-Prediction
Project Overview
This project aims to build a machine learning model to predict customer churn for a telecom company. Customer churn prediction helps companies identify customers who are likely to leave, allowing them to take proactive measures to retain them and improve overall customer satisfaction.

Objectives
Data Exploration: Analyze customer data to identify patterns and features associated with churn.
Model Building: Develop a predictive model to classify customers as likely to churn or not.
Model Evaluation: Assess the model’s performance using various metrics and visualizations.
Deployment: Create a user-friendly interface for real-time predictions.
Technologies Used
Python: Programming language used for data analysis and model building.
Pandas: Data manipulation and analysis library.
Scikit-learn: Machine learning library for model training and evaluation.
Logistic Regression: Machine learning model used for prediction.
Streamlit: Framework used for building the web application.
Pickle: Serialization library used for saving and loading the model.
Data
The dataset used in this project includes information about customer demographics, account information, and usage patterns. The primary objective is to predict whether a customer will churn based on these features.

Features
Numerical Features: tenure, MonthlyCharges, TotalCharges
Categorical Features: gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod
Model
A Logistic Regression model was trained and evaluated for this project. The model was chosen for its interpretability and effectiveness in binary classification problems.

Evaluation
The model’s performance was evaluated using:

Accuracy
Precision
Recall
F1-score
ROC AUC
Deployment
The model is deployed using a Streamlit app, which allows users to input customer details and receive predictions about the likelihood of churn.
