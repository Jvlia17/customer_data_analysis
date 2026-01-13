import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# --- konfiguracja połączenia ---
DB_USER = "postgres"
DB_PASSWORD = "your_password_here" #!!!
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "mydb"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# --- pobranie danych z PostgreSQL ---
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

print("Podgląd danych:")
print(df.head())

# --- przygotowanie danych ---
X = df.drop(columns=["responded", "customer_id"])
y = df["responded"]

X = X.select_dtypes(include=["number"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- pipeline ML ---
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

pipeline.fit(X_train, y_train)

# --- ewaluacja ---
y_pred = pipeline.predict(X_test)

print("\nWyniki modelu:")
print(classification_report(y_test, y_pred))
