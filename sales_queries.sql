-- Table Schema
CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    order_date DATE NOT NULL,
    product_category VARCHAR(50),
    quantity INT,
    order_amount_inr DECIMAL(10,2),
    payment_method VARCHAR(30),
    delivery_status VARCHAR(20)
);

-- KPI 1: Monthly Revenue & Order Volume Breakdown
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS order_month,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(order_amount_inr), 2) AS monthly_revenue,
    ROUND(AVG(order_amount_inr), 2) AS avg_order_value
FROM orders
WHERE delivery_status = 'Delivered'
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY order_month ASC;

-- KPI 2: Top 2 Spending Customers per Product Category (Window Function)
WITH CustomerCategorySpend AS (
    SELECT 
        customer_id,
        product_category,
        SUM(order_amount_inr) AS total_spent,
        DENSE_RANK() OVER (
            PARTITION BY product_category 
            ORDER BY SUM(order_amount_inr) DESC
        ) AS customer_rank
    FROM orders
    WHERE delivery_status = 'Delivered'
    GROUP BY customer_id, product_category
)
SELECT 
    product_category,
    customer_id,
    ROUND(total_spent, 2) AS total_spent
FROM CustomerCategorySpend
WHERE customer_rank <= 2;

-- KPI 3: Cancellation and Return Rates by Payment Method
SELECT 
    payment_method,
    COUNT(order_id) AS total_attempts,
    ROUND(SUM(CASE WHEN delivery_status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(order_id), 2) AS cancellation_rate_pct,
    ROUND(SUM(CASE WHEN delivery_status = 'Returned' THEN 1 ELSE 0 END) * 100.0 / COUNT(order_id), 2) AS return_rate_pct
FROM orders
GROUP BY payment_method
ORDER BY cancellation_rate_pct DESC;