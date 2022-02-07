-- 1) Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, catalogs и products в 
-- таблицу logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа и содержимое поля name.
DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	id BIGINT,
	table_n VARCHAR (250),
	date_time DATETIME,
	name VARCHAR(250))
	ENGINE = ARCHIVE;

DROP TRIGGER IF EXISTS users_trg;
delimiter //
CREATE TRIGGER users_trg AFTER INSERT ON users
FOR EACH ROW
BEGIN
	INSERT INTO logs (id, table_n,date_time ,name)
	VALUES (NEW.id,'users',NOW(),NEW.name);
END //

DROP TRIGGER IF EXISTS catalogs_trg;
delimiter //
CREATE TRIGGER catalogs_trg AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	INSERT INTO logs (id, table_n, date_time, name)
	VALUES (NEW.id,'catalogs',NOW(),NEW.name);
END //

DROP TRIGGER IF EXISTS products_trg;
delimiter //
CREATE TRIGGER products_trg AFTER INSERT ON products
FOR EACH ROW
BEGIN
	INSERT INTO logs (id, table_n, date_time, name)
	VALUES (NEW.id,'products',NOW(),NEW.name);
END //

delimiter ;

INSERT INTO users (name, birthday_at)
VALUES 
('Max', '1989-02-15'),
('Anna','1989-02-15'),
('Nick', '1989-02-15');

INSERT INTO catalogs (name)
VALUES 
('Электроника'),
('Товары для дома'),
('Спорттовары');

INSERT INTO products (name)
VALUES
('Монитор'),
('Процессор'),
('Видеокарта');

-- 2) Создайте SQL-запрос, который помещает в таблицу users миллион записей.
-- Миллион очень уж долго выполняется, поставил ограничение на тысячу
DROP TABLE IF EXISTS million_cnt;
CREATE TABLE million_cnt (
	num BIGINT
);
DROP PROCEDURE IF EXISTS million;
DELIMITER //
CREATE PROCEDURE million ()
BEGIN
	DECLARE i INT DEFAULT 0;
		WHILE i < 1000 DO
			INSERT INTO million_cnt (num)
			VALUES (1);
			SET i = i + 1;
		END WHILE;
end //

DELIMITER ;
CALL million(); 
