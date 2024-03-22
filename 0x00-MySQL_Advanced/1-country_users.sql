-- Task Description: Write a SQL script that creates a table users with specific attributes including an enumeration for country
-- If the table already exists, the script should not fail

-- Create table users with required attributes including an enumeration for country
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

