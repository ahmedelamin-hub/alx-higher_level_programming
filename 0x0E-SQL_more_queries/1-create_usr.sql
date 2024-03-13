-- 1-create_user.sql
-- Attempt to grant privileges to the user, implicitly creating them if they do not exist.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' WITH GRANT OPTION;
