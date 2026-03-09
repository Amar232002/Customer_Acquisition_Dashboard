-- Customer Acquisition Analysis Queries

-- 1. Monthly Acquisition Trend
SELECT 
    DATE_FORMAT(acquisition_date, '%Y-%m') AS month,
    COUNT(*) AS new_customers,
    SUM(total_spent) AS revenue
FROM customers
GROUP BY month
ORDER BY month DESC;

-- 2. Churn Rate by Segment
SELECT 
    customer_segment,
    COUNT(*) AS total,
    SUM(churned) AS churned_count,
    ROUND(AVG(churned) * 100, 2) AS churn_rate
FROM customers
GROUP BY customer_segment;

-- 3. Revenue by Segment
SELECT 
    customer_segment,
    COUNT(*) AS customers,
    SUM(total_spent) AS total_revenue,
    AVG(total_spent) AS avg_revenue
FROM customers
GROUP BY customer_segment
ORDER BY total_revenue DESC;

-- 4. Top 10 Customers
SELECT 
    customer_id,
    customer_name,
    total_spent,
    purchase_count
FROM customers
ORDER BY total_spent DESC
LIMIT 10;

-- 5. Acquisition by Channel
SELECT 
    acquisition_channel,
    COUNT(*) AS customers,
    SUM(total_spent) AS revenue
FROM customers
GROUP BY acquisition_channel
ORDER BY revenue DESC;