-- ============================================
-- DATAPULSE BUSINESS ANALYTICS
-- ============================================

-- 1. Total Revenue
SELECT
    SUM(revenue) AS total_revenue
FROM sales_data;


-- 2. Total Orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM sales_data;


-- 3. Average Order Value
SELECT
    ROUND(AVG(revenue), 2) AS average_order_value
FROM sales_data;


-- 4. Revenue by Month
SELECT
    order_month,
    SUM(revenue) AS monthly_revenue
FROM sales_data
GROUP BY order_month
ORDER BY order_month;


-- 5. Revenue by Customer
SELECT
    customer_id,
    customer_name,
    SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY customer_id, customer_name
ORDER BY total_revenue DESC;


-- 6. Top Products
SELECT
    product_name,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY product_name
ORDER BY total_revenue DESC;


-- 7. Order Status Analysis
SELECT
    status,
    COUNT(*) AS order_count,
    SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY status
ORDER BY order_count DESC;


-- 8. Monthly Order Count
SELECT
    order_month,
    COUNT(DISTINCT order_id) AS total_orders
FROM sales_data
GROUP BY order_month
ORDER BY order_month;