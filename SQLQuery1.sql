CREATE DATABASE php_hardcore_project;

use php_hardcore_project;

create table Student(
username varchar(30),
password varchar(40) not null,
fullname varchar(30),
email varchar(30),
phonenum varchar(10),
id int IDENTITY(1,1) primary key,
)

create table Teacher(
id int IDENTITY(1,1),
username varchar(30),
password varchar(40) not null,
primary key(id, password),
)


insert into Student (username, password, fullname, email, phonenum )
values ('ngocht','168910','Hoang Thi Ngoc','ngochths150417@fpt.edu.vn',0349361014),
		('nampxh','1234','Pham Xuan Hoai Nam','nampxhhe151338@fpt.edu.vn',012356723);

insert into Teacher (username, password)
values ('ducdm','admin'),
    ('flag','DBS{IA1601_GROUP2_FLAG2}'),
	('anhht','123');
	('binh','123');
	
select * from Teacher
select * from Student