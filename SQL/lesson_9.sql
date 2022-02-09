/* Практическое задание по теме “Транзакции, переменные, 
 * представления”
 */

-- 1. В базе данных shop и sample присутствуют одни и те же таблицы, 
-- учебной базы данных. Переместите запись id = 1 из таблицы shop.users 
-- в таблицу sample.users. Используйте транзакции.


START TRANSACTION;

select @id1 := id, @name1 := name from gb.users where id = 1;

insert into sample.users (id, name)
VALUES (@id1, @name1);
commit;

delete from sample.users where id = 1;
-- 2. Создайте представление, которое выводит название name товарной 
-- позиции из таблицы products и соответствующее название каталога
-- name из таблицы catalogs.
drop view if exists view1;
create view view1 (prod_name, cat_name) as select p.name, c.name from products as p
join catalogs c on p.catalog_id = c.id;

select * from view1;

/* Практическое задание 
 * по теме “Хранимые процедуры и функции, триггеры" */

-- Создайте хранимую функцию hello(), которая будет возвращать приветствие, 
-- в зависимости от текущего времени суток. С 6:00 до 12:00 функция должна 
-- возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать 
-- фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — 
-- "Доброй ночи".
DELIMITER //
drop procedure if exists hello//
create procedure hello()
begin
	if (date_format(now(), '%h:%s') > '06:00' 
	and date_format(now(), '%h:%s') < '12:00') then 
		select 'Доброе утро';
	elseif (date_format(now(), '%h:%s') > '12:00' 
	and date_format(now(), '%h:%s') < '18:00') then 
		select ('Добрый день');
	elseif (date_format(now(), '%h:%s') > '18:00' 
	and date_format(now(), '%h:%s') < '00:00') then 
		select 'Добрый вечер';
	else
		select 'Доброй ночи';
	end if;
end//

call hello()//

/* В таблице products есть два текстовых поля: name с названием товара и 
 * description с его описанием. Допустимо присутствие обоих полей или одно 
 * из них. Ситуация, когда оба поля принимают неопределенное значение NULL 
 * неприемлема. Используя триггеры, добейтесь того, чтобы одно из этих полей 
 * или оба поля были заполнены. При попытке присвоить полям NULL-значение 
 * необходимо отменить операцию.*/
DROP TRIGGER IF EXISTS trig1;
delimiter //
CREATE TRIGGER trig1 BEFORE INSERT ON products
FOR EACH ROW
BEGIN
	IF (NEW.desription is null and NEW.name is null) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ошибка тригера. Оба значения null!';
	END IF;
END //

insert into gb.products (name, desription, price)
values ('name1', null, 5000)//

insert into gb.products (name, desription, price)
values (null, null, 5000)//


