import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# --- Database connection settings ---
DB_USER = "postgres"
DB_PASSWORD = "your_password_here" #!!!
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "customer_data_analysis"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# --- Load data from PostgreSQL ---
query = """
SELECT
    c.customer_id,
    c.age,
    c.annual_income,
    c.tenure_months,
    c.credit_limit,
    c.current_balance,
    c.num_products,
    o.responded
FROM customers c
JOIN offers o ON c.customer_id = o.customer_id;
"""

df = pd.read_sql(query, engine)

print("Dataset preview:")
print(df.head())

# --- Prepare features and target variable ---
X = df.drop(columns=["responded", "customer_id"])
y = df["responded"]

# Keep only numerical features
X = X.select_dtypes(include=["number"])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Build the machine learning pipeline ---
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

# Train the model
pipeline.fit(X_train, y_train)

# --- Evaluate model performance ---
y_pred = pipeline.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
