-- create new table called uniqe_id where id must be uniqe
CREATE TABLE IF NOT EXISTS `uniqe_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
