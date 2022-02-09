DROP DATABASE IF EXISTS vk;
CREATE DATABASE vk;
USE vk;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY, 
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password_hash varchar(100),
    phone BIGINT,
    is_deleted bit default 0,
    INDEX users_firstname_lastname_idx(firstname, lastname)
);

DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles (
	user_id SERIAL PRIMARY KEY,
    gender CHAR(1),
    birthday DATE,
	photo_id BIGINT UNSIGNED,
    created_at DATETIME DEFAULT NOW(),
    hometown VARCHAR(100)
    
);

ALTER TABLE profiles ADD CONSTRAINT fk_user_id
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE ON DELETE CASCADE;
   
DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
	id SERIAL PRIMARY KEY,
	from_user_id BIGINT UNSIGNED NOT NULL,
    to_user_id BIGINT UNSIGNED NOT NULL,
    body TEXT,
    created_at DATETIME DEFAULT NOW(),

    FOREIGN KEY (from_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (to_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS friend_requests;
CREATE TABLE friend_requests (
	
	initiator_user_id BIGINT UNSIGNED NOT NULL,
    target_user_id BIGINT UNSIGNED NOT NULL,
    status ENUM('requested', 'approved', 'declined', 'unfriended'),
	requested_at DATETIME DEFAULT NOW(),
	updated_at DATETIME on update now(),
	
    PRIMARY KEY (initiator_user_id, target_user_id),
    FOREIGN KEY (initiator_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (target_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS communities;
CREATE TABLE communities(
	id SERIAL PRIMARY KEY,
	name VARCHAR(150),
	admin_user_id BIGINT UNSIGNED,

	INDEX communities_name_idx(name),
	FOREIGN KEY (admin_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS users_communities;
CREATE TABLE users_communities(
	user_id BIGINT UNSIGNED NOT NULL,
	community_id BIGINT UNSIGNED NOT NULL,
  
	PRIMARY KEY (user_id, community_id), 
    FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (community_id) REFERENCES communities(id) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS media_types;
CREATE TABLE media_types(
	id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS media;
CREATE TABLE media(
	id SERIAL PRIMARY KEY,
    media_type_id BIGINT UNSIGNED,
    user_id BIGINT UNSIGNED NOT NULL,
  	body text,
    filename VARCHAR(255),
    `size` INT,
	metadata JSON,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (media_type_id) REFERENCES media_types(id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    media_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(id) ON UPDATE CASCADE ON DELETE CASCADE

);

DROP TABLE IF EXISTS `photo_albums`;
CREATE TABLE `photo_albums` (
	`id` SERIAL,
	`name` VARCHAR(255) DEFAULT NULL,
    `user_id` BIGINT UNSIGNED DEFAULT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE SET NULL,
  	PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `photos`;
CREATE TABLE `photos` (
	id SERIAL PRIMARY KEY,
	`album_id` BIGINT UNSIGNED NOT NULL,
	`media_id` BIGINT UNSIGNED NOT NULL,

	FOREIGN KEY (album_id) REFERENCES photo_albums(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(id) ON UPDATE CASCADE ON DELETE CASCADE
);

ALTER TABLE `profiles` ADD CONSTRAINT fk_photo_id
    FOREIGN KEY (photo_id) REFERENCES photos(id)
    ON UPDATE CASCADE ON DELETE SET NULL;

   
   
-- 1-M
DROP TABLE IF EXISTS gift;
CREATE TABLE gift (
	id SERIAL PRIMARY KEY,
	from_user_id BIGINT UNSIGNED,
	to_user_id BIGINT UNSIGNED,
	mess TEXT, -- сообщение к подарку
	created_at DATETIME DEFAULT NOW(),
	FOREIGN KEY (from_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (to_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE SET NULL 
);

DROP TABLE IF EXISTS marital_status;  -- семейное положение
CREATE TABLE marital_status(
	m_user_id BIGINT UNSIGNED NOT NULL,
	f_user_id BIGINT UNSIGNED NOT NULL,
	 
	PRIMARY KEY (m_user_id, f_user_id),
	FOREIGN KEY (m_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (f_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- 1-1
DROP TABLE IF EXISTS personal_data;
CREATE TABLE personal_data(  -- персональные данные пользователя(скрытые)
	user_id SERIAL PRIMARY KEY,
	pers_data JSON,	
	FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);



-- M-M

DROP TABLE IF EXISTS games;
CREATE TABLE games (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	INDEX games_name_ind(name)
);


DROP TABLE IF EXISTS games_users;
CREATE TABLE games_users(
	games_id BIGINT UNSIGNED NOT NULL,
	users_id BIGINT UNSIGNED NOT NULL,
	
	PRIMARY KEY (users_id, games_id),
	FOREIGN KEY (games_id) REFERENCES games(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (users_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
	
);


   
