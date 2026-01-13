-- =========================
-- 1. TABELA: CUSTOMERS
-- =========================
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    age INT NOT NULL,
    annual_income NUMERIC(12,2),
    tenure_months INT,
    credit_limit NUMERIC(12,2),
    current_balance NUMERIC(12,2),
    num_products INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- 2. TABELA: OFFERS
-- =========================
CREATE TABLE offers (
    offer_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    offer_date DATE,
    responded INT CHECK (responded IN (0, 1)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- =========================
-- 3. TABELA: TRANSACTIONS (opcjonalna, bardzo bankowa)
-- =========================
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    transaction_date DATE,
    amount NUMERIC(12,2),
    transaction_type VARCHAR(20),
    CONSTRAINT fk_transaction_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- =========================
-- 4. INDEKSY (ważne w praktyce)
-- =========================
CREATE INDEX idx_customers_income ON customers(annual_income);
CREATE INDEX idx_offers_customer ON offers(customer_id);
CREATE INDEX idx_transactions_customer ON transactions(customer_id);
