-- =====================================================
-- RETAIL STORE INVENTORY SYSTEM
-- =====================================================

-- =====================================================
-- 1. DROP EXISTING TABLES (if they exist)
-- =====================================================
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;

-- =====================================================
-- 2. CREATE TABLES
-- =====================================================

-- Categories Table
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(150) NOT NULL,
    CategoryID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL CHECK (Price > 0),
    StockQuantity INT DEFAULT 0 CHECK (StockQuantity >= 0),
    Supplier VARCHAR(100),
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Sales Table
CREATE TABLE Sales (
    SalesID INT PRIMARY KEY AUTO_INCREMENT,
    ProductID INT NOT NULL,
    QuantitySold INT NOT NULL CHECK (QuantitySold > 0),
    SalePrice DECIMAL(10, 2) NOT NULL,
    TotalAmount DECIMAL(12, 2) NOT NULL,
    SalesDate DATE NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- =====================================================
-- 3. INSERT DATA INTO CATEGORIES
-- =====================================================
INSERT INTO Categories (CategoryName, Description) VALUES
('Electronics', 'Electronic devices and gadgets'),
('Clothing', 'Apparel and fashion items'),
('Home & Kitchen', 'Kitchen appliances and home decor'),
('Sports & Outdoors', 'Sports equipment and outdoor gear'),
('Books & Media', 'Books, DVDs, and digital media');

-- =====================================================
-- 4. INSERT DATA INTO PRODUCTS
-- =====================================================
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity, Supplier) VALUES
-- Electronics
('Laptop Dell XPS 13', 1, 1299.99, 15, 'Dell Inc.'),
('iPhone 15 Pro', 1, 999.99, 25, 'Apple Inc.'),
('Samsung 4K TV 55"', 1, 599.99, 10, 'Samsung Electronics'),
('Wireless Headphones Sony', 1, 349.99, 40, 'Sony Corporation'),
('USB-C Cable 2m', 1, 19.99, 200, 'Cable Tech Ltd.'),

-- Clothing
('Cotton T-Shirt Men', 2, 29.99, 100, 'Fashion World'),
('Jeans Blue Denim', 2, 79.99, 80, 'Denim Co.'),
('Winter Jacket', 2, 149.99, 35, 'Winter Wear Inc.'),
('Sports Shoes Running', 2, 119.99, 60, 'Athletic Shoes Ltd.'),
('Summer Dress', 2, 59.99, 50, 'Fashion World'),

-- Home & Kitchen
('Coffee Maker', 3, 89.99, 30, 'Kitchen Masters'),
('Non-Stick Pan Set', 3, 64.99, 45, 'Cookware Co.'),
('Blender Pro', 3, 79.99, 25, 'Kitchen Masters'),
('Wall Clock Modern', 3, 34.99, 70, 'Decor Plus'),
('Bed Sheets Set', 3, 49.99, 100, 'Home Comfort'),

-- Sports & Outdoors
('Yoga Mat', 4, 24.99, 80, 'Fitness Gear'),
('Bicycle Mountain', 4, 499.99, 12, 'Bike World'),
('Camping Tent', 4, 199.99, 20, 'Outdoor Adventures'),
('Dumbbell Set', 4, 99.99, 50, 'Fitness Gear'),

-- Books & Media
('The Great Gatsby Book', 5, 14.99, 60, 'Publishers Inc.'),
('Python Programming DVD', 5, 39.99, 30, 'Tech Education'),
('Harry Potter Series', 5, 49.99, 45, 'Publishers Inc.');

-- =====================================================
-- 5. INSERT DATA INTO SALES
-- =====================================================
INSERT INTO Sales (ProductID, QuantitySold, SalePrice, TotalAmount, SalesDate) VALUES
-- Electronics Sales
(1, 2, 1299.99, 2599.98, '2025-11-01'),
(2, 5, 999.99, 4999.95, '2025-11-02'),
(3, 1, 599.99, 599.99, '2025-11-03'),
(4, 3, 349.99, 1049.97, '2025-11-04'),
(5, 10, 19.99, 199.90, '2025-11-05'),

-- Clothing Sales
(6, 15, 29.99, 449.85, '2025-11-06'),
(7, 8, 79.99, 639.92, '2025-11-07'),
(8, 4, 149.99, 599.96, '2025-11-08'),
(9, 12, 119.99, 1439.88, '2025-11-09'),
(10, 6, 59.99, 359.94, '2025-11-10'),

-- Home & Kitchen Sales
(11, 5, 89.99, 449.95, '2025-11-01'),
(12, 8, 64.99, 519.92, '2025-11-02'),
(13, 3, 79.99, 239.97, '2025-11-03'),
(14, 12, 34.99, 419.88, '2025-11-04'),
(15, 20, 49.99, 999.80, '2025-11-05'),

-- Sports & Outdoors Sales
(16, 18, 24.99, 449.82, '2025-11-06'),
(17, 2, 499.99, 999.98, '2025-11-07'),
(18, 3, 199.99, 599.97, '2025-11-08'),
(19, 7, 99.99, 699.93, '2025-11-09'),

-- Books & Media Sales
(20, 25, 14.99, 374.75, '2025-11-01'),
(21, 8, 39.99, 319.92, '2025-11-02'),
(22, 10, 49.99, 499.90, '2025-11-03');

-- =====================================================
-- 6. VERIFY DATA INSERTION
-- =====================================================
SELECT COUNT(*) as 'Total Categories' FROM Categories;
SELECT COUNT(*) as 'Total Products' FROM Products;
SELECT COUNT(*) as 'Total Sales' FROM Sales;

-- =====================================================
-- 7. CALCULATE TOTAL SALES PER CATEGORY
-- =====================================================
SELECT 
    c.CategoryID,
    c.CategoryName,
    COUNT(s.SalesID) as 'Number of Transactions',
    SUM(s.QuantitySold) as 'Total Quantity Sold',
    ROUND(SUM(s.TotalAmount), 2) as 'Total Sales Amount',
    ROUND(AVG(s.TotalAmount), 2) as 'Average Sale Amount'
FROM Categories c
LEFT JOIN Products p ON c.CategoryID = p.CategoryID
LEFT JOIN Sales s ON p.ProductID = s.ProductID
GROUP BY c.CategoryID, c.CategoryName
ORDER BY ROUND(SUM(s.TotalAmount), 2) DESC;

-- =====================================================
-- 8. ADDITIONAL USEFUL QUERIES
-- =====================================================

-- Top 5 Best-Selling Products
SELECT 
    p.ProductID,
    p.ProductName,
    c.CategoryName,
    SUM(s.QuantitySold) as 'Total Sold',
    ROUND(SUM(s.TotalAmount), 2) as 'Revenue'
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
LEFT JOIN Sales s ON p.ProductID = s.ProductID
GROUP BY p.ProductID, p.ProductName, c.CategoryName
ORDER BY 'Total Sold' DESC
LIMIT 5;

-- Sales by Date
SELECT 
    s.SalesDate,
    COUNT(s.SalesID) as 'Transaction Count',
    ROUND(SUM(s.TotalAmount), 2) as 'Daily Total'
FROM Sales s
GROUP BY s.SalesDate
ORDER BY s.SalesDate DESC;

-- Product Stock Status
SELECT 
    p.ProductID,
    p.ProductName,
    c.CategoryName,
    p.Price,
    p.StockQuantity,
    CASE 
        WHEN p.StockQuantity <= 10 THEN 'Low Stock'
        WHEN p.StockQuantity <= 30 THEN 'Medium Stock'
        ELSE 'Good Stock'
    END as 'Stock Status'
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
ORDER BY p.StockQuantity ASC;
