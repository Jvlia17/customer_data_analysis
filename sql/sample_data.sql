-- =========================
-- CUSTOMERS (100 rows)
-- =========================

INSERT INTO customers (age, annual_income, tenure_months, credit_limit, current_balance, num_products)
SELECT
    (18 + floor(random() * 60))::int AS age,
    (30000 + random() * 120000)::numeric(12,2) AS annual_income,
    (6 + floor(random() * 180))::int AS tenure_months,
    (5000 + random() * 75000)::numeric(12,2) AS credit_limit,
    (0 + random() * 30000)::numeric(12,2) AS current_balance,
    (1 + floor(random() * 5))::int AS num_products
FROM generate_series(1, 100);

-- =========================
-- OFFERS (REALISTIC RESPONSE LOGIC)
-- =========================

WITH customer_features AS (
    SELECT
        c.customer_id,
        c.age,
        c.annual_income,
        c.credit_limit,
        c.current_balance,
        c.num_products,

        (c.current_balance / NULLIF(c.credit_limit, 0)) AS utilization_ratio
    FROM customers c
)

INSERT INTO offers (customer_id, offer_date, responded)
SELECT
    customer_id,
    (DATE '2026-01-01' + (random() * 30)::int) AS offer_date,

    -- REALISTIC RESPONSE MODEL (NOT RANDOM)
    CASE
        WHEN (
            -- HIGH INCOME increases response
            annual_income > 70000

            -- LOW utilization increases response
            AND utilization_ratio < 0.5

            -- more products = more engagement
            AND num_products >= 2

        )
        OR (
            -- medium probability group
            annual_income > 50000
            AND random() < 0.4
        )
        THEN 1
        ELSE 0
    END AS responded

FROM customer_features;

-- =========================
-- TRANSACTIONS (3 per customer approx)
-- =========================

INSERT INTO transactions (customer_id, transaction_date, amount, transaction_type)
SELECT
    c.customer_id,
    (DATE '2025-12-01' + (random() * 60)::int) AS transaction_date,

    CASE
        WHEN random() < 0.5
        THEN -(100 + random() * 2000)   -- purchase
        ELSE (100 + random() * 3000)    -- payment
    END AS amount,

    CASE
        WHEN random() < 0.5 THEN 'purchase'
        ELSE 'payment'
    END AS transaction_type

FROM customers c
CROSS JOIN generate_series(1, 3);
