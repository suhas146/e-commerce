CREATE DATABASE MARKET;
USE MARKET;
CREATE TABLE products (
    id INT PRIMARY KEY,
    cost DECIMAL(10, 5),
    category VARCHAR(100),
    name TEXT,
    brand VARCHAR(50),
    retail_price DECIMAL(10, 2),
    department VARCHAR(50),
    sku VARCHAR(100),
    distribution_center_id INT
);
DESCRIBE TABLE PRODUCTS;
SELECT * FROM PRODUCTS;
DROP TABLE PRODUCTS;
SELECT COUNT(*) FROM products;

