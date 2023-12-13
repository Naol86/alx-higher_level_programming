-- create new table called uniqe_id where id must be uniqe
CREATE TABLE IF NOT EXISTS `uniqe_id`(
	`id` INT UNIQUE DEFAULT 1,
	`name` VARCHAR(256)
);
