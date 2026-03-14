CREATE DATABASE IF NOT EXISTS amazon_analysis;

USE amazon_analysis;

CREATE TABLE amazon_products (
product_id VARCHAR(50),
product_name TEXT,
category TEXT,
discounted_price FLOAT,
actual_price FLOAT,
discount_percentage VARCHAR(10),
rating FLOAT,
rating_count INT
);

-- Top rated products
SELECT product_name, rating
FROM amazon_products
ORDER BY rating DESC
LIMIT 10;

-- Most reviewed products
SELECT product_name, rating_count
FROM amazon_products
ORDER BY rating_count DESC
LIMIT 10;

-- Highest discounts
SELECT product_name,
(actual_price - discounted_price) AS discount
FROM amazon_products
ORDER BY discount DESC
LIMIT 10;

-- Average rating by category
SELECT category, AVG(rating)
FROM amazon_products
GROUP BY category
ORDER BY AVG(rating) DESC;
