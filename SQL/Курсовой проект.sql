/* Это база данных о футболе. Она содержит имена футболистов, тренеров, названия лиг и клубов, бюджет клубов, награды футболистов и так далее.
 * Она поможет быстрее находить ту или иную информацию.
 * Задачи, которые будут решены:
 * 1. Найти клубы, футболисты которых обладают какими-либо наградами.
 * 2. Сколько французов играет в Английской Премьер лиге.
 * 3. В каких клубах играют футболисты, стоимость которых более 200 млн долларов
 * 4.  В какиих лигах играют 3 футболиста с наименьшей ценой
 * 5. Какие награды, у футболистов, которых тренирует Маурицио Почетинно
 * 6. Какая суммарная стоимость у футболистов Францусской Лиги 1
 */

DROP DATABASE IF EXISTS footb_db;
CREATE DATABASE footb_db;
USE footb_db;
DROP TABLE IF EXISTS players;
CREATE TABLE players (
	id SERIAL PRIMARY KEY, 
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    p_position VARCHAR (20),
    birthday DATE,
    p_number INT,
    nation VARCHAR(100),
    price INT COMMENT 'В миллионах долларов',
    INDEX players_firstname_lastname_idx(firstname, lastname)
);

DROP TABLE IF EXISTS leagues;
CREATE TABLE leagues (
	id SERIAL PRIMARY KEY,
	name VARCHAR (100)
);

DROP TABLE IF EXISTS clubs;
CREATE TABLE clubs (
	id SERIAL PRIMARY KEY,
	name VARCHAR (100),
	budget INT COMMENT 'Миллионов долларов',
	league_id BIGINT UNSIGNED,
	FOREIGN KEY (league_id) REFERENCES leagues(id) ON UPDATE CASCADE ON DELETE SET NULL
);

ALTER TABLE players 
ADD club_id BIGINT UNSIGNED;
ALTER TABLE players 
ADD FOREIGN KEY (club_id) REFERENCES clubs(id);

DROP TABLE IF EXISTS coach;
CREATE TABLE coach (
	 id SERIAL PRIMARY KEY,
	 name VARCHAR (100),
	 club_id BIGINT UNSIGNED,
	 cnt_trof INT COMMENT 'количество трофеев',
	 FOREIGN KEY (club_id) REFERENCES clubs(id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS transfer_list;
CREATE TABLE tranfer_list (
	id SERIAL PRIMARY KEY,
	player_id BIGINT UNSIGNED,
	from_club_id BIGINT UNSIGNED,
	to_club_id BIGINT UNSIGNED,
	price_t INT COMMENT 'В миллионах долларов',
	FOREIGN KEY (player_id) REFERENCES players(id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY (from_club_id) REFERENCES clubs(id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY (to_club_id) REFERENCES clubs(id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS nations;
CREATE TABLE nations(
	nation_id SERIAL PRIMARY KEY,
	nation VARCHAR (100)
);

DROP TABLE IF EXISTS nation_teams;
CREATE TABLE nation_teams(
	nation_id BIGINT UNSIGNED,
	player_id BIGINT UNSIGNED,
	PRIMARY KEY (nation_id, player_id),
	FOREIGN KEY (nation_id) REFERENCES nations(nation_id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (player_id) REFERENCES players(id) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS awards;
CREATE TABLE awards(
	id SERIAL PRIMARY KEY,
	name VARCHAR (100)
);

DROP TABLE IF EXISTS awards_players;
CREATE TABLE awards_players (
	player_id BIGINT UNSIGNED, 
	awards_id BIGINT UNSIGNED,
	cnt INT,
	PRIMARY KEY (player_id, awards_id),
	FOREIGN KEY (player_id) REFERENCES players(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (awards_id) REFERENCES awards(id) ON UPDATE CASCADE ON DELETE CASCADE
);
-- Наполнение

INSERT INTO footb_db.leagues (name)
VALUES 
('Английская Премьер лига'),
('Испанская Премера'),
('Французская Лига 1'),
('Российская Премьер лига'),
('Немецкая Бундес лига'),
('Итальянская Серия А'),
('Бразилская Высшая лига'),
('Российская ФНЛ'),
('Голландская Евердизи'),
('Французский Второй дивизион');

INSERT INTO footb_db.leagues (id, name)
VALUES (999,'Свободный агент');

INSERT INTO footb_db.clubs (name, budget, league_id)
VALUES
('PSG', 9000, 3),
('Liverpool', 500, 1),
('Man united', 800, 1),
('Barcelona', 350, 2),
('Totenhem', 300, 1),
('ЦСКА', 90, 4),
('Real Madrid', 550, 2),
('Marcel', 210, 3),
('Bayer 04', 435, 5),
('Milan', 650, 6);

INSERT INTO footb_db.clubs (id, name, league_id)
VALUES (999, 'Свободный агент',999);

INSERT INTO footb_db.players
(id,firstname, lastname, p_position, birthday, p_number, price, nation, club_id)
VALUES
(1,'Kylian', 'Mbape', 'striker', '1999-03-21', 7, 750, 'Франция',1),
(2,'Kile', 'Wallker', 'defender', '1990-01-30', 3, 50, 'Англия', 2),
(3,'Lionel', 'Messi', 'striker', '1987-08-21', 10, 250, 'Аргентина',1),
(4,'Junior', 'Neymar', 'striker', '1997-07-14', 9, 450, 'Бразилия',1),
(5,'Roberto', 'Firmino', 'striker', '1995-05-18', 11, 80, 'Бразилия',2),
(6,'Rafael', 'Varan', 'defender', '1989-10-24', 16, 110, 'Франция',3),
(7,'Marc_Andre', 'ter Stegen', 'goalkeeper', '1990-11-17', 1, 200, 'Германия',4),
(8,'Hugo', 'Lloris', 'goalkeeper', '1996-02-04', 45, 70, 'Франция',5),
(9,'Игорь', 'Акинфеев', 'goalkeeper', '1990-06-15', 1, 20, 'Россия',6);


INSERT INTO coach (name, club_id, cnt_trof)
VALUES
('Зинедин Зидан', 999, 15),
('Карло Анчелотти', 7, 12),
('Маурицио Почетинно', 1, 9),
('Томас Тухель', 5, 13),
('Василий Березуцкий', 6, 0),
('Юрген Клоп', 2, 20),
('Сер Алекс Фергюсон', 3, 25),
('Хави', 4, 0),
('Херардо Сеоане', 3, 9),
('Стефано Пиоли', 10, 8);


INSERT INTO nations (nation, nation_id)
VALUES
('Франция', 1),
('Англия',2),
('Бразилия', 3),
('Германия', 4),
('Аргентина', 5),
('Россия', 6),
('Италия',7),
('Испания',8),
('Турция', 9),
('Алжир', 10);


INSERT INTO nation_teams (player_id,nation_id)
VALUES 
(1,1),
(2,2),
(3,5),
(4,3),
(5,3),
(6,1),
(7,4),
(8,1),
(9,6);

INSERT INTO tranfer_list (player_id, from_club_id, to_club_id, price_t)
VALUES 
(3, 4, 1, 0),
(2,3,2, 15),
(1,1,7, 650),
(6,7,3, 100),
(9, 10, 6, 1),
(7, 2, 4, 2),
(4,4,1, 40);

INSERT INTO awards (name)
VALUES 
('Золотой мяч'),
('Золотая бутца'),
('Приз Льва Яшина'),
('Бомбардир года'),
('Чемпион лиги'),
('Лучший защитник');

INSERT INTO awards_players (player_id, awards_id, cnt)
VALUES 
(1, 1, 3),
(1,4,6),
(2, 6, 1),
(9, 3, 10),
(6, 6,8),
(5, 2, 2),
(3,1,8),
(3, 4, 6),
(4, 2, 3),
(4,4, 2);

-- Задачи

-- 1. Найти клубы, футболисты которых обладают какими-либо наградами.

SELECT c.name, p.lastname, a.name FROM clubs c 
JOIN players p ON c.id = p.club_id 
JOIN awards_players ap ON ap.player_id = p.id
JOIN awards a ON ap.awards_id = a.id
ORDER BY p.lastname;

-- 2.Сколько французов играет в Английской Премьер лиге.
SELECT COUNT(*), l.name FROM players p 
JOIN clubs c ON p.club_id = c.id 
JOIN leagues l ON l.id = c.league_id
JOIN nation_teams nt ON nt.player_id = p.id 
JOIN nations n ON n.nation_id = nt.nation_id 
WHERE l.id = 1 AND n.nation_id = 1;
-- 3. В каких клубах играют футболисты, стоимость которых более 200 млн долларов
SELECT p.lastname, c.name, p.price FROM players p 
JOIN clubs c ON p.club_id = c.id 
WHERE p.price >= 200
ORDER BY p.price DESC;
-- 4. В каких лигах играют 3 футболистa с наименьшей ценой
SELECT l.name, p.lastname, p.price FROM leagues l 
JOIN clubs c ON c.league_id = l.id 
JOIN players p on p.club_id = c.id 
ORDER BY p.price LIMIT 3;

-- 5. Какие награды, у футболистов, которых тренирует Маурицио Почетинно
SELECT c.name, p.lastname, a.name  FROM coach c 
JOIN clubs c2 ON c.club_id = c2.id 
JOIN players p ON p.club_id = c2.id 
JOIN awards_players ap ON ap.player_id = p.id 
JOIN awards a ON a.id = ap.awards_id 
WHERE c.name = 'Маурицио Почетинно';

-- 6. Какая суммарная стоимость у футболистов Францусской Лиги 1
SELECT (SUM(p.price) *1000000) as price FROM players p 
JOIN clubs c ON c.id = p.club_id 
JOIN leagues l ON l.id = c.league_id 
WHERE l.id = 3;

-- Создадим представление, которое будет содержать 3 лучших тренеров (по количеству трофеев), их клубы и игрока этого клуба

DROP VIEW IF EXISTS top_coach;
CREATE VIEW top_coach (coach, cnt_trof, club, players) AS 
SELECT c.name,c.cnt_trof, c2.name, p.lastname FROM coach c
LEFT JOIN clubs c2 on c2.id = c.club_id 
LEFT JOIN players p on p.club_id = c2.id 
GROUP BY c.name
ORDER BY c.cnt_trof DESC LIMIT 3;


SELECT * FROM top_coach;

-- Создадим представление, которое будет содержать фамилию игрока, название и количество наград, его клуб и старну

DROP VIEW IF EXISTS v_players;
CREATE VIEW v_players (lastname, n_award, cnt_awards, club, nation) AS 
SELECT p.lastname, a.name, ap.cnt, c.name, n.nation FROM players p 
JOIN awards_players ap ON ap.player_id = p.id 
JOIN awards a ON a.id = ap.awards_id 
JOIN clubs c ON c.id = p.club_id 
JOIN nation_teams nt ON nt.player_id = p.id 
JOIN nations n ON n.nation_id = nt.nation_id
ORDER BY p.lastname;

SELECT * FROM v_players;


-- Создадим процедуру, которая будет проверять возможность покупки клубом игрока


DROP PROCEDURE IF EXISTS transfer;
DELIMITER //
CREATE PROCEDURE transfer(IN player_id BIGINT, IN club_id BIGINT)
BEGIN
	SET @p_id = player_id, @c_id = club_id;
	IF ((SELECT price FROM players WHERE id = @p_id) <= (SELECT budget FROM clubs WHERE id = @c_id)) THEN
		SET @res = 'Трасфер осуществим';
	ELSE 
		SET @res ='Трансфер невозможен;';
	END IF;
	SELECT @res;
END//


DELIMITER ;
CALL transfer(1,1);
CALL transfer(1,2);

-- Создадим функцию, которая будет считать какой бюджет останетс у клуба после трансфера игрока
DROP FUNCTION IF EXISTS tr_budget;
DELIMITER //
CREATE FUNCTION tr_budget (club_id BIGINT, player_id BIGINT)
RETURNS INT DETERMINISTIC
BEGIN
	DECLARE p_price, c_budget, res INT;
	SET p_price = (SELECT price FROM players WHERE id = player_id);
	SET c_budget = (SELECT budget FROM clubs WHERE id = club_id);
	SET res = c_budget - p_price;
  RETURN (res);
END

SELECT tr_budget (1,4);
SELECT tr_budget (2,2);

-- Создадим триггер, которые проверяет, наличие имени и фамилии у добавляемого игрока

DROP TRIGGER IF EXISTS tran_check;
DELIMITER //
CREATE TRIGGER tran_chek BEFORE INSERT ON players
FOR EACH ROW
BEGIN
	IF ((NEW.firstname IS NULL)  and (NEW.lastname IS NULL)) THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ошибка. Добавление игрока без имени и фамилии';
	END IF;
END//
DELIMITER ;

INSERT INTO players (firstname, lastname)
VALUES (NULL, NULL);

-- Добавим триггер, который проверяет, что после обновления у тренера не стало меньше трофеев.

DROP TRIGGER IF EXISTS coach_check;
DELIMITER //
CREATE TRIGGER coach_chek BEFORE UPDATE ON coach
FOR EACH ROW
BEGIN
	IF (NEW.cnt_trof < OLD.cnt_trof) THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ошибка. У тренера стало меньше наград. Это невозможно';
	END IF;
END//
DELIMITER ;

UPDATE coach 
SET cnt_trof = 11
WHERE id = 4;








