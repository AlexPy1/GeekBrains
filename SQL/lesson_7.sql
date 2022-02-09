-- 1. Составьте список пользователей users, 
-- которые осуществили хотя бы один заказ orders в интернет магазине
alter table orders 
change user_id user_id BIGINT UNSIGNED DEFAULT NULL;


alter table orders 
add foreign key (user_id)
references users (id)
on update cascade
on delete cascade;

insert into orders (id, user_id)
values
(1,2),
(2,4),
(3,6);

select u.id, u.name from users as u
join
	orders as o
where u.id = o.user_id;

-- 2 Выведите список товаров 
-- products и разделов catalogs, который соответствует товару.
alter table products 
change catalog_id catalog_id BIGINT UNSIGNED DEFAULT NULL;

alter table products 
add foreign key (catalog_id)
references catalogs (id)
on update cascade
on delete cascade;

select p.name, c.name from products as p
join
	catalogs as c
where p.catalog_id = c.id;
