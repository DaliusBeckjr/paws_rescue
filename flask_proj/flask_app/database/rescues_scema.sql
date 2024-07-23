CREATE DATABASE IF NOT EXISTS paws_rescue_schema
DEFAULT CHARACTER SET = 'utf8mb4';

USE paws_rescue_schema;

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    password VARVHAR(80),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- name, description, breed, location, age, gender, size, fixed, type, created_at, updated_at
DROP TABLE IF EXISTS rescues;
CREATE TABLE rescues(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description TEXT, 
    breed VARCHAR(255),
    location VARCHAR(255),
    age INTEGER,
    gender INTEGER,
    size INTEGER,
    fixed INTEGER,
    type INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);