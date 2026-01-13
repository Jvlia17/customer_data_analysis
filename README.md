# Banking CRM Analytics – SQL & Python

End-to-end analytics project simulating a banking CRM use case.

## Project Overview
The project analyzes customer behavior and predicts response to credit offers using:
- PostgreSQL (relational database, SQL analytics)
- Python (Pandas, scikit-learn)
- Logistic Regression model

## Database
The database consists of:
- customers
- offers
- transactions

Schema and sample data are provided in the `/sql` directory.

## Machine Learning
A logistic regression model is trained to predict whether a customer will respond to a credit offer based on:
- income
- tenure
- credit utilization
- product ownership

## How to Run
1. Create PostgreSQL database
2. Run SQL scripts from `/sql`
3. Configure DB credentials in `main.py`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
