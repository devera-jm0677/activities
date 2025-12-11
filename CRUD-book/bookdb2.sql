-- Create the database
-- ON DUPLICATE KEY UPDATE
-- needs to correct platform dialect problem
CREATE DATABASE IF NOT EXISTS bookdb2;

-- Use the database
USE bookdb2;

-- Create the books table
CREATE TABLE IF NOT EXISTS book (
    isbn INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    publisher VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL
);

-- Insert sample data
INSERT INTO book (isbn, title, publisher, category) VALUES
(1001, 'To Kill a Mockingbird', 'HarperCollins', 'Fiction'),
(1002, 'A Brief History of Time', 'Bantam Books', 'Science'),
(1003, 'The Art of War', 'Penguin Books', 'History')
ON DUPLICATE KEY UPDATE isbn=isbn;