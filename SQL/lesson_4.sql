/* Заполнить все таблицы БД vk данными (по 10-100 записей в каждой таблице).
*/
USE vk

 -- Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке.
SELECT distinct  firstname
FROM users
ORDER BY firstname;

-- Первые пять пользователей пометить как удаленные.

UPDATE users 
SET 
	is_deleted = 0
LIMIT 5
	
-- Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней).

delete from messages
where created_at > NOW();
	

-- Написать название темы курсового проекта.
-- Я еще не определился, постараюсь прикрепить к следущему дз.
	