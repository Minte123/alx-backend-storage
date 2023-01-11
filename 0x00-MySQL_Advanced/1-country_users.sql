-- SQL script to create a table users
-- attributes: 'id', 'email', 'name', 'country'
-- country is enum with 'US' as default and never null
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `name` VARCHAR(255),
  `country` ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
