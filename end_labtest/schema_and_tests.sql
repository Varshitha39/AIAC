-- schema_and_tests.sql
-- MySQL-compatible schema, example queries, and test data for a book shop
-- Contains: authors, books, books_authors, sales, sale_items

-- NOTE: Run this file in a development database. The script truncates tables
-- for test data; do NOT run against production data.

-- Drop tables in dependency order for clean re-run
DROP TABLE IF EXISTS sale_items;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS books_authors;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- 1) Authors
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 2) Books
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    publisher VARCHAR(200),
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00, -- current list price
    stock INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 3) Join table: books <-> authors (many-to-many)
CREATE TABLE books_authors (
    book_id INT NOT NULL,
    author_id INT NOT NULL,
    contribution VARCHAR(100),
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 4) Sales (one row per transaction/order)
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    customer_name VARCHAR(255),
    total_amount DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 5) Sale items: items inside a sale. unit_price is copied at sale time.
CREATE TABLE sale_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    line_total DECIMAL(12,2) AS (quantity * unit_price) STORED,
    FOREIGN KEY (sale_id) REFERENCES sales(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE RESTRICT,
    INDEX (book_id),
    INDEX (sale_id)
) ENGINE=InnoDB;

-- =====================
-- Useful queries
-- =====================

-- A) List best-selling books by units sold (top N)
-- Replace 10 with desired limit
-- Returns: book id, title, isbn, units_sold, revenue
SELECT
    b.id,
    b.title,
    b.isbn,
    SUM(si.quantity) AS units_sold,
    SUM(si.quantity * si.unit_price) AS revenue
FROM sale_items si
JOIN books b ON b.id = si.book_id
GROUP BY b.id, b.title, b.isbn
ORDER BY units_sold DESC, revenue DESC
LIMIT 10;

-- B) List best-selling books by revenue (top N)
SELECT
    b.id,
    b.title,
    b.isbn,
    SUM(si.quantity * si.unit_price) AS revenue,
    SUM(si.quantity) AS units_sold
FROM sale_items si
JOIN books b ON b.id = si.book_id
GROUP BY b.id, b.title, b.isbn
ORDER BY revenue DESC
LIMIT 10;

-- C) Best-selling in a date range (e.g., last 30 days)
SELECT
    b.id,
    b.title,
    SUM(si.quantity) AS units_sold
FROM sale_items si
JOIN sales s ON s.id = si.sale_id
JOIN books b ON b.id = si.book_id
WHERE s.sale_date >= NOW() - INTERVAL 30 DAY
GROUP BY b.id, b.title
ORDER BY units_sold DESC
LIMIT 10;

-- D) Best-selling authors (aggregate across their books)
SELECT
    a.id,
    CONCAT(a.first_name, ' ', a.last_name) AS author_name,
    SUM(si.quantity) AS units_sold,
    SUM(si.quantity * si.unit_price) AS revenue
FROM sale_items si
JOIN books b ON b.id = si.book_id
JOIN books_authors ba ON ba.book_id = b.id
JOIN authors a ON a.id = ba.author_id
GROUP BY a.id, author_name
ORDER BY units_sold DESC
LIMIT 10;

-- =====================
-- Write operations
-- =====================

-- 1) Add a new author (simple)
INSERT INTO authors (first_name, last_name, bio)
VALUES ('Jane', 'Doe', 'Author of sample books');

-- Get last inserted id (MySQL client)
SELECT LAST_INSERT_ID() AS new_author_id;

-- MySQL 8.0.27+ supports RETURNING:
-- INSERT INTO authors (first_name, last_name, bio)
-- VALUES ('Jane','Doe','Author of sample books') RETURNING id;

-- 2) Update stock safely (decrement when fulfilling an order)
-- Example: decrement stock for book id = ? by ? (use parameter binding in app)
-- Atomic approach using WHERE stock >= qty
-- In application code: run inside transaction, check affected rows
START TRANSACTION;
-- replace 42 and 3 with real values
UPDATE books
SET stock = stock - 3
WHERE id = 42 AND stock >= 3;
-- In client: check ROW_COUNT() (or use affected_rows API). If 0 -> insufficient stock
-- Example check in SQL (for manual testing):
SELECT ROW_COUNT() AS rows_updated;
COMMIT;

-- Pessimistic-locking approach
START TRANSACTION;
SELECT stock FROM books WHERE id = 42 FOR UPDATE;
-- application logic verifies stock and then updates
UPDATE books SET stock = stock - 3 WHERE id = 42;
COMMIT;

-- =====================
-- Test data and verification queries
-- =====================
-- WARNING: the following truncates tables and inserts sample data for testing.
-- Use only in a dev database.

-- Disable FK checks to allow truncation order
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE sale_items;
TRUNCATE TABLE sales;
TRUNCATE TABLE books_authors;
TRUNCATE TABLE books;
TRUNCATE TABLE authors;
SET FOREIGN_KEY_CHECKS = 1;

-- Insert sample authors
INSERT INTO authors (first_name, last_name, bio) VALUES
('Alice','Smith','Author of fiction'),
('Bob','Jones','Non-fiction writer'),
('Carol','White','Children''s books author');

-- Insert sample books
INSERT INTO books (title, isbn, publisher, price, stock) VALUES
('Fictional Tales','978-0000000001','Acme Pub',12.99,50),
('Practical Things','978-0000000002','Acme Pub',20.00,20),
('Kids Fun','978-0000000003','KidsPub',8.50,100);

-- Link authors to books
INSERT INTO books_authors (book_id, author_id, contribution) VALUES
(1,1,'author'),
(2,2,'author'),
(3,3,'author'),
(3,1,'co-author');

-- Insert sample sales
INSERT INTO sales (sale_date, customer_name, total_amount) VALUES
('2025-11-15 10:00:00','Customer A',25.98),
('2025-11-16 14:00:00','Customer B',29.49),
('2025-11-18 09:30:00','Customer C',8.50);

-- Insert sample sale items
INSERT INTO sale_items (sale_id, book_id, quantity, unit_price) VALUES
(1,1,2,12.99),
(2,2,1,20.00),
(2,3,1,9.49),
(3,3,1,8.50);

-- Verification queries (expected results in comments)

-- 1) Units sold per book
-- Expected: Fictional Tales -> 2, Kids Fun -> 2, Practical Things -> 1
SELECT b.title, SUM(si.quantity) AS units_sold
FROM sale_items si JOIN books b ON b.id = si.book_id
GROUP BY b.id, b.title
ORDER BY units_sold DESC, b.title;

-- 2) Revenue per book
SELECT b.title, SUM(si.quantity * si.unit_price) AS revenue
FROM sale_items si JOIN books b ON b.id = si.book_id
GROUP BY b.id, b.title
ORDER BY revenue DESC;

-- 3) Top authors by units sold (Alice has book 1 and co-authored book 3)
SELECT CONCAT(a.first_name,' ',a.last_name) AS author_name, SUM(si.quantity) AS units_sold
FROM sale_items si
JOIN books b ON b.id = si.book_id
JOIN books_authors ba ON ba.book_id = b.id
JOIN authors a ON a.id = ba.author_id
GROUP BY a.id
ORDER BY units_sold DESC;

-- 4) Test add author
INSERT INTO authors (first_name, last_name, bio) VALUES ('Dora','Miles','New author');
SELECT LAST_INSERT_ID() AS new_author_id;

-- 5) Test safe stock decrement (try to decrease book id 1 by 3)
START TRANSACTION;
UPDATE books SET stock = stock - 3 WHERE id = 1 AND stock >= 3;
SELECT ROW_COUNT() AS rows_updated; -- expect 1
COMMIT;
SELECT id, title, stock FROM books WHERE id = 1;

-- 6) Test insufficient stock scenario (attempt large decrement)
START TRANSACTION;
UPDATE books SET stock = stock - 999 WHERE id = 2 AND stock >= 999;
SELECT ROW_COUNT() AS rows_updated; -- expect 0
COMMIT;
SELECT id, title, stock FROM books WHERE id = 2;

-- End of file
