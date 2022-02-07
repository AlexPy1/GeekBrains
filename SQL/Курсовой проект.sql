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
	budget INT,
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
	price_t INT,
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
('Зидедин Зидан', 999, 15),
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
(2,3,2, 15000000),
(1,1,7, 650000000),
(6,7,3, 100000000),
(9, 10, 6, 500000),
(7, 2, 4, 1500000),
(4,4,1, 40000000);

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