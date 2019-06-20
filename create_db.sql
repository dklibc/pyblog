use pyblog;

drop table if exists main;

drop table if exists note;

create table main (
	session_id char(22),
	session_start timestamp
);

insert into main (session_id, session_start) values (null,null);

create table note (
	id int unsigned auto_increment primary key,
	title varchar(255) not null,
	body text,
	pub_date timestamp,
	views int unsigned default 0
);
