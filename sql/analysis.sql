-- Preview the first customer records with their offer response
SELECT c.customer_id, c.age, c.annual_income, o.responded
FROM customers c
JOIN offers o ON c.customer_id = o.customer_id;

-- Count customers who responded and did not respond to the offer
SELECT responded, COUNT(*) AS num_customers
FROM offers
GROUP BY responded;

-- Compare the average credit limit by offer response
SELECT o.responded, AVG(c.credit_limit) AS avg_credit_limit
FROM customers c
JOIN offers o ON c.customer_id = o.customer_id
GROUP BY o.responded;

-- Calculate the total transaction amount for each customer
-- and compare it with their offer response
SELECT c.customer_id,
       SUM(t.amount) AS total_transactions,
       o.responded
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
JOIN offers o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, o.responded
ORDER BY total_transactions DESC;

-- Segment customers by age group
SELECT CASE
         WHEN age < 30 THEN 'Young'
         WHEN age BETWEEN 30 AND 50 THEN 'Middle-aged'
         ELSE 'Senior'
       END AS age_segment,
       COUNT(*) AS num_customers,
       AVG(c.annual_income) AS avg_income
FROM customers c
GROUP BY age_segment;
