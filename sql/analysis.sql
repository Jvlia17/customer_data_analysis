-- Podgląd pierwszych 10 klientów z ofertą
SELECT c.customer_id, c.age, c.annual_income, o.responded
FROM customers c
JOIN offers o ON c.customer_id = o.customer_id;

-- Ile klientów odpowiedziało na ofertę, a ile nie
SELECT responded, COUNT(*) AS num_customers
FROM offers
GROUP BY responded;

SELECT o.responded, AVG(c.credit_limit) AS avg_credit_limit
FROM customers c
JOIN offers o ON c.customer_id = o.customer_id
GROUP BY o.responded;

-- Suma transakcji dla każdego klienta i jego odpowiedź na ofertę
SELECT c.customer_id,
       SUM(t.amount) AS total_transactions,
       o.responded
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
JOIN offers o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, o.responded
ORDER BY total_transactions DESC;

-- Tworzymy segmenty klientów wg wieku
SELECT CASE
         WHEN age < 30 THEN 'Young'
         WHEN age BETWEEN 30 AND 50 THEN 'Middle'
         ELSE 'Senior'
       END AS age_segment,
       COUNT(*) AS num_customers,
       AVG(c.annual_income) AS avg_income
FROM customers c
GROUP BY age_segment;
