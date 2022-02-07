-- 1. Подсчитайте средний возраст пользователей в таблице users.
use vk

select AVG((TO_DAYS(NOW()) - TO_DAYS(birthday)) / 365.25) AS age FROM profiles;

/* 2. Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
 Следует учесть, что необходимы дни недели текущего года, а не года рождения.*/

SELECT 
	DAYNAME(CONCAT(YEAR(NOW()), '-', SUBSTRING(birthday, 6, 10))) AS days,
	COUNT(*) AS count_days
FROM 
	profiles
GROUP BY 
    days
ORDER BY
	count_days DESC;



/*  В прошлом дз Вы мне написали "3 задание - если у нас не будет в 
  базе пользователя с id=2, то Ваш скрипт будет решать задачу?", действительно,
  нужно было испльзовать LIMIT 5, ошибку понял
 */
