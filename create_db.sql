use pyblog;

drop table if exists blog;
drop table if exists note;

create table blog (
	login varchar(30) not null default 'pyblog_user',
	pwd varchar(20) not null default 'pyblog_user'
);

create table note (
	id int unsigned auto_increment primary key,
	title varchar(255) not null,
	body text,
	pub_date timestamp,
	views int unsigned default 0
);
