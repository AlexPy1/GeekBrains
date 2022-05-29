/* 1. Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, который указывался при установке.
*/
/* C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 39
Server version: 8.0.27 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> */

-- 2.Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.


USE example;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

-- 3.Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.


/*C:\WINDOWS\system32>cd C:\Program Files\MySQL\MySQL Server 8.0\bin

C:\Program Files\MySQL\MySQL Server 8.0\bin>mysqldump example > example12.sql
C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql sample < example12.sql

C:\Program Files\MySQL\MySQL Server 8.0\bin>*/
