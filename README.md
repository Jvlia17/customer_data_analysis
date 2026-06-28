# Banking CRM Analytics – SQL & Python

End-to-end analytics project simulating a banking CRM use case.

## 🔷 Project Overview
This project simulates a banking CRM analytics use case focused on improving the effectiveness of credit offer targeting.

In many banking systems, credit offers are distributed broadly across customer bases, which leads to low conversion rates and inefficient marketing spend. The goal of this project is to analyze customer behavior and build a predictive model that helps identify customers most likely to respond to credit offers.

The solution combines SQL-based data processing with Python-based analytics and machine learning.

## 🎯 Business Problem

Banks often rely on non-targeted or loosely segmented marketing campaigns when distributing credit offers. This results in:
- low response rates
- high acquisition costs
- inefficient use of customer data

This project addresses the need for data-driven targeting by identifying behavioral and financial patterns associated with customer responsiveness.

## 🗄️ Data & Database Design
The dataset simulates a banking CRM system and consists of three main tables:

- customers – demographic and financial information
- offers – credit offer details and response labels
- transactions – customer transaction history

The data is structured in a relational PostgreSQL database.
Schema and sample data are available in the /sql directory.

## ⚙️ SQL Feature Engineering

Customer-level features were created using SQL, including:

- aggregated transaction behavior (spending patterns, frequency)
- credit utilization metrics
- tenure-based features
- product ownership indicators
- customer-level joins between transactional and CRM data

SQL logic uses joins and aggregations to transform raw transactional data into analytical features for modeling.

## 📊 EDA

Exploratory Data Analysis was used to understand customer behavior and identify patterns related to offer response.

Key areas analyzed:

- distribution of income and credit utilization
- response rate across customer segments
- relationship between tenure and engagement
- correlation between financial behavior and offer acceptance

## 🤖 Predictive Model
A logistic regression model was trained to predict whether a customer will respond to a credit offer.

Features used:
- income
- tenure
- credit utilization
- product ownership
- aggregated transaction behavior

The model was trained using a standard train/test split and evaluated on a holdout dataset.

## 🔍 Key Insights

- Customers with higher credit utilization show a higher likelihood of responding to credit offers
- Product ownership is strongly associated with increased engagement
- Longer-tenure customers tend to be less responsive to new credit offers
- Transaction activity patterns provide additional predictive signal beyond static attributes

## 💼 Business Recommendations

- Prioritize credit offers for high-utilization customers to increase conversion rates
- Use product ownership as a segmentation feature in CRM campaigns
- Reduce marketing exposure for low-propensity long-tenure customers
- Incorporate behavioral transaction features into targeting models to improve accuracy

## 🚀 How to Run
1. Create PostgreSQL database
2. Run SQL scripts from `/sql`
3. Configure DB credentials in `main.py`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
