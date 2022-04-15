-- 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.

USE VK 
ALTER TABLE users ADD created_at datetime;
ALTER TABLE users ADD updated_at datetime;

UPDATE users 
set created_at = NOW();

UPDATE users 
set updated_at = NOW();

/* 2 Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и 
 в них долгое время помещались значения в формате 20.10.2017 8:10. 
Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.
*/

ALTER TABLE users DROP created_at;
ALTER TABLE users DROP updated_at;
ALTER TABLE users ADD created_at varchar(100);
ALTER TABLE users ADD updated_at varchar(100);

UPDATE users 
set created_at = '20.10.2017 8:10' ;

UPDATE users 
set updated_at = '21.10.2017 9:40';

ALTER TABLE users ADD created_at_new DATETIME; 
ALTER TABLE users ADD updated_at_new DATETIME;
UPDATE users
SET created_at_new = STR_TO_DATE(created_at, '%d.%m.%Y %h:%i'),
    updated_at_new = STR_TO_DATE(updated_at, '%d.%m.%Y %h:%i');
ALTER TABLE users 
    DROP created_at, DROP updated_at, 
    RENAME COLUMN created_at_new TO created_at, RENAME COLUMN updated_at_new TO updated_at;
   
/* 3. В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, 
 если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом, 
 чтобы они выводились в порядке увеличения значения value. Однако нулевые запасы должны выводиться в конце, после всех записей.
 */

DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  value INT
);

INSERT INTO
  storehouses_products (name, value)
VALUES
  ('ваза', 45),
  ('подушка', 60),
  ('кастрюля', 0),
  ('ноутбук', 10),
  ('кровать', 3),
  ('мышка', 13),
  ('одеяло', 0);
 
SELECT * FROM storehouses_products 
ORDER BY value = 0, value;

SELECT ROUND(AVG(TIMESTAMPDIFF(YEAR, birthday, NOW())), 0) AS AVG_Age FROM profiles;

