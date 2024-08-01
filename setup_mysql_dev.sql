-- Create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creating user if doesn't exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant permissions
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
