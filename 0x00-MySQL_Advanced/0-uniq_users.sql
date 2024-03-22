-- Task Description: Write a SQL script that creates a table users with specific attributes
-- If the table already exists, the script should not fail
-- Context: Making the email attribute unique directly in the table schema enforces business rules and avoids bugs in applications

-- Create table users with required attributes
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

