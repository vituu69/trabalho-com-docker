CREATE DATABASE test;

CREATE TABLE IF NOT EXISTS 'test'.'users'(
    id INT AUTO_INCREMENT PRIMARY KEY
    name VARCHAR(255) NOT NULL
) ENGINE=INNODB;