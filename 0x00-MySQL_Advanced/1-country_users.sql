-- This script create a table called users
-- with the following columns:
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) NOT NULL UNIQUE,
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
