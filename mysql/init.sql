-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS fastapi_mvc;
USE fastapi_mvc;

-- Drop user if exists and create new one
DROP USER IF EXISTS 'fastapi_user'@'%';
CREATE USER 'fastapi_user'@'%' IDENTIFIED BY 'fastapi_password';

-- Grant all necessary privileges for SQLAlchemy to work
GRANT ALL PRIVILEGES ON fastapi_mvc.* TO 'fastapi_user'@'%';
GRANT REFERENCES ON fastapi_mvc.* TO 'fastapi_user'@'%';

-- Set password expiration to never
ALTER USER 'fastapi_user'@'%' PASSWORD EXPIRE NEVER;

-- Flush privileges to apply changes
FLUSH PRIVILEGES; 