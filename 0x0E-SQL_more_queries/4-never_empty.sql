-- A script that creates the table id_not_null in a mysql server
-- id_not_null description:id INT with the default value 1, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table id_not_null already exists, script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT default 1, name VARCHAR(256));
