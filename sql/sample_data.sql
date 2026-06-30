INSERT INTO customers (age, annual_income, tenure_months, credit_limit, current_balance, num_products)
VALUES
(25, 50000, 12, 10000, 2000, 2),
(40, 120000, 60, 50000, 15000, 3),
(30, 80000, 24, 20000, 5000, 1),
(55, 150000, 120, 80000, 20000, 4);

INSERT INTO offers (customer_id, offer_date, responded)
VALUES
(1, '2026-01-01', 1),
(2, '2026-01-05', 0),
(3, '2026-01-10', 1),
(4, '2026-01-12', 0);

INSERT INTO transactions (customer_id, transaction_date, amount, transaction_type)
VALUES
(1, '2025-12-01', 1500, 'payment'),
(1, '2025-12-15', -300, 'purchase'),
(2, '2025-12-05', 2000, 'payment'),
(3, '2025-12-10', -500, 'purchase'),
(4, '2025-12-12', -1200, 'purchase'),
(4, '2025-12-20', 2500, 'payment');
