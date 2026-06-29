# Banking CRM Analytics – SQL & Python

End-to-end data science project simulating a banking CRM use case focused on predicting customer response to credit offers.

---

## 🔷 Project Overview
This project demonstrates an end-to-end analytics workflow built on relational data stored in PostgreSQL.

The goal is to predict whether a customer will respond to a credit offer based on behavioral and financial attributes.

The project combines:

- SQL for data storage, joins, and feature extraction
- Python (pandas) for data processing and feature engineering
- scikit-learn for machine learning modeling
- visualization for model evaluation and interpretation

---

## 🎯 Business Problem

Banks and financial institutions frequently send credit offers to large customer bases, resulting in low response rates and inefficient marketing spend.

The objective of this project is to build a predictive model that identifies customers who are more likely to respond to a credit offer, improving targeting efficiency.

---

## 🗄️ Data
The project uses a PostgreSQL relational database with three tables:

- **customers** – demographic and financial attributes
- **offers** – credit offer records with binary response label (`responded`)
- **transactions** – transaction history (stored but not used in final model)

---

## ⚙️ Data Extraction

Data is extracted from PostgreSQL using SQL JOINs between `customers` and `offers`.

Additional feature engineering is performed in Python to enrich the dataset with behavioral financial metrics.

### Engineered features include:

- `utilization_ratio` = current_balance / credit_limit  
- `income_to_credit` = annual_income / credit_limit  
- `risk_score` = composite financial risk indicator

---

## 🤖 Model
A **Random Forest Classifier** is used to model customer response behavior.

### Pipeline:

- Feature engineering (Python)
- Train/test split (80/20, stratified)
- Random Forest model (n_estimators=300, max_depth=6, class_weight="balanced")

---

## 📊 Evaluation
Model performance is evaluated using:

- Precision / Recall / F1-score
- Confusion Matrix
- ROC Curve
- ROC-AUC score

Final Results

- **Accuracy:** ~0.61  
- **ROC-AUC:** ~0.69  
- Balanced performance across both classes (0 and 1)

<p align="center">
  <img src="https://github.com/user-attachments/assets/dd462b5b-bf6a-4803-b0bc-6bc37dd8ed82" width="450">
  <img src="https://github.com/user-attachments/assets/013a98da-7c13-4760-a0cf-e61a7b5c3db2" width="450">
</p>

<img width="1380" height="498" alt="obraz3" src="https://github.com/user-attachments/assets/e452cde4-8168-4078-b479-8fe78e496dd3" />

---

## 📈 Key Insights

- Customer annual income and risk score are strongest predictors of response
- Financial utilization patterns significantly influence classification decisions
- The model captures moderate predictive signal, indicating realistic noise in synthetic data

---

## 🚀 How to Run
1. Create PostgreSQL database
2. Run SQL scripts from `/sql`
3. Configure DB credentials in `main.py`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
5. Run pipeline 
   ```bash
   python main.py
