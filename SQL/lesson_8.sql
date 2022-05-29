-- 1.Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите
-- человека, который больше всех общался с нашим пользователем.

-- пусть id =1 
USE vk

select m.from_user_id, concat(u.firstname, " ", u.lastname) as name, 
count(*) as cnt 
from messages m
join users u on u.id=m.from_user_id 
join friend_requests fr on (fr.initiator_user_id = m.from_user_id and 
fr.target_user_id =1) or (fr.target_user_id = m.from_user_id and fr.initiator_user_id=1)
where fr.status = 'approved'
group by m.from_user_id
order by confirmed_at 
limit 1;





-- 2.Подсчитать общее количество лайков, которые получили пользователи младше 11 лет.
select count(*)
from likes l
join media m on m.id =l.media_id 
join profiles p on p.user_id = m.user_id 
where TIMESTAMPDIFF (year, p.birthday, NOW()) < 11;

-- 3.Определить кто больше поставил лайков (всего): мужчины или женщины.

select count(*) from likes l
join profiles p on p.user_id = l.user_id
group by p.gender;

DELIMITER //
drop procedure if exists hello//
create procedure hello ()
begin
	if (1<2) then 
		select 'Доброе утро' as a;
	else
		select 'saad' as v;
	end if;
end//
call hello ();




DROP TRIGGER IF EXISTS trig1;
delimiter //
CREATE TRIGGER trig1 BEFORE INSERT ON products
FOR EACH ROW
BEGIN
	IF (NEW.desription is null and NEW.name is null) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ошибка  тригера';
	END IF;
END //





