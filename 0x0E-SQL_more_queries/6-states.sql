-- create database called hbtn_0d_usa and table called states in that database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states`(
	`id` INT NOT NULL AUTOINCREMENT,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY(`id`)
);
