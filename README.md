# Banking CRM Analytics – SQL & Python

End-to-end data science project simulating a banking CRM use case focused on predicting customer response to credit offers.

## 🔷 Project Overview
This project demonstrates a basic workflow for building a predictive model using relational data stored in PostgreSQL.

The goal is to predict whether a customer will respond to a credit offer based on available customer attributes.

The project combines:

- SQL for data extraction
- Python (pandas) for data processing
- scikit-learn for machine learning

## 🎯 Business Problem

Banks often send credit offers to a broad customer base, which results in low response rates and inefficient marketing spend.

This project aims to build a simple predictive model that helps identify customers who are more likely to respond to a credit offer.

## 🗄️ Data
The project uses a PostgreSQL database with three tables:

- customers – customer demographic and financial data
- offers – credit offer records with response label (responded)
- transactions – transaction history (defined in schema but not used in the model)

## ⚙️ Data Extraction

Data for modeling is extracted using a SQL JOIN between customers and offers.

Only customer attributes and the response label are used in the machine learning model.

## 🤖 Model
A logistic regression model is used to predict customer response.

Pipeline:
- StandardScaler (feature scaling)
- LogisticRegression (class_weight="balanced")

Features used:
- age
- annual_income
- tenure_months
- credit_limit
- current_balance
- num_products

Training:
- Train/test split (80/20)
- Random state set for reproducibility

## 📊 Evaluation

Model performance is evaluated using:

- precision
- recall
- f1-score

Results are displayed using classification_report.

## 🚀 How to Run
1. Create PostgreSQL database
2. Run SQL scripts from `/sql`
3. Configure DB credentials in `main.py`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
