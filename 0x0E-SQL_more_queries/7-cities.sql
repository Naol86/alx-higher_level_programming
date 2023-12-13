-- create database named hbtn_0d_usa and table cities in it
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	`id` INT NOT NULL UNIQUE AUTO_INCREMENT,
	PRIMARY key(`id`),
	`state_id` INT NOT NULL,
	FOREIGN KEY (`state_id`) REFERENCES `states`(`id`),
	`name` VARCHAR(256) NOT NULL
);
