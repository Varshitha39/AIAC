-- Create a sample database
CREATE DATABASE SampleDB;

-- Use the newly created database
USE SampleDB;

-- Create a sample table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    HireDate DATE
);

-- Insert sample data
INSERT INTO Employees (FirstName, LastName, Email, HireDate) VALUES
('John', 'Doe', 'john.doe@example.com', '2022-01-15'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-03-22');