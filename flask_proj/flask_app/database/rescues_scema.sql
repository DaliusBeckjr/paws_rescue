CREATE DATABASE IF NOT EXISTS paws_rescue_schema
DEFAULT CHARACTER SET = 'utf8mb4';

USE paws_rescue_schema;

DROP TABLE IF EXISTS users;

-- first_name, last_name, email, password, created_at, updated_at
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
    address VARCHAR(255),
    age INTEGER,
    gender INTEGER,
    size INTEGER,
    fixed INTEGER,
    type INTEGER,
    image_path VARCHAR(255), -- store file path or url
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_id INT, 
    FOREIGN KEY (user_id) REFERENCES users(id)
);


-- maybe: add a likes feature for each user to like a specific animal
-- maybe: add a part where we can add images to the specific data

DROP TABLE IF EXISTS likes
CREATE TABLE likes(
    user_id INT,
    rescue_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (rescue_id) REFERENCES rescues(id)
);


-- if we created a table we can always alter it just by saing

-- ALTER TABLE users
-- ADD birthdate DATE;

-- to add multiple columns we would say
-- ALTER TABLE users
-- ADD COLUMN phone_number VARCHAR(15),
-- ADD COLUMN birthdate DATE;