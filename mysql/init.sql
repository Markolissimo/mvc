CREATE DATABASE IF NOT EXISTS fastapi_mvc;
USE fastapi_mvc;

DROP USER IF EXISTS 'fastapi_user'@'%';
CREATE USER 'fastapi_user'@'%' IDENTIFIED BY 'fastapi_password';

GRANT ALL PRIVILEGES ON fastapi_mvc.* TO 'fastapi_user'@'%';
GRANT REFERENCES ON fastapi_mvc.* TO 'fastapi_user'@'%';

ALTER USER 'fastapi_user'@'%' PASSWORD EXPIRE NEVER;

FLUSH PRIVILEGES; 