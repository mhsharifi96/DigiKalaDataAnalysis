# DATABASE


### what is schema?
Schema  is a collection of logical structures of data. In PostgreSQL, schema is a named collection of tables, views, functions, constraints, indexes,sequences etc.

----

## Create Database 
```
createdb testdb
```


## Create Tables
```
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_contraint,
   column2 datatype(length) column_contraint,
   column3 datatype(length) column_contraint,
   table_constraints
);
```

```
CREATE TABLE sample (
	user_id serial ,
	username VARCHAR ( 50 ) ,
	password VARCHAR ( 50 ) ,
	email VARCHAR ( 255 ) ,
	created_on TIMESTAMP ,
    last_login TIMESTAMP 
);
```

```CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP 
);
```

```CREATE TABLE fruits(
   id SERIAL PRIMARY KEY,
   vname VARCHAR(5) NOT NULL,
    cname CHAR(5) NOT NULL```
    
```

## ALTER 
```
CREATE TABLE "user"(
    "id" INTEGER NOT NULL,
    "firstname" INTEGER NOT NULL,
    "lastname" INTEGER NOT NULL
);
ALTER TABLE
    "user" ADD PRIMARY KEY("id");
    
CREATE TABLE "lesson"(
    "id" INTEGER NOT NULL,
    "name" CHAR(255) NOT NULL
);
ALTER TABLE
    "lesson" ADD PRIMARY KEY("id");
CREATE TABLE "mark"(
    "id" INTEGER NOT NULL,
    "lesson_id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL
);
ALTER TABLE
    "mark" ADD PRIMARY KEY("id");
ALTER TABLE
    "mark" ADD CONSTRAINT "mark_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "mark" ADD CONSTRAINT "mark_lesson_id_foreign" FOREIGN KEY("lesson_id") REFERENCES "lesson"("id");
```

## CRUD

```
DROP TABLE IF EXISTS courses;

CREATE TABLE courses(
	course_id serial primary key,
	course_name VARCHAR(255) NOT NULL,
	description VARCHAR(500),
	published_date date
);

INSERT INTO 
	courses(course_name, description, published_date)
VALUES
	('PostgreSQL for Developers','A complete PostgreSQL for Developers','2020-07-13'),
	('PostgreSQL Admininstration','A PostgreSQL Guide for DBA',NULL),
	('PostgreSQL High Performance',NULL,NULL),
	('PostgreSQL Bootcamp','Learn PostgreSQL via Bootcamp','2013-07-11'),
	('Mastering PostgreSQL','Mastering PostgreSQL in 21 Days','2012-06-30');
```

update : 
```
UPDATE courses
SET published_date = '2020-08-01' 
WHERE course_id = 3;

-- OR
UPDATE courses
SET published_date = '2020-07-01'
WHERE course_id = 2
RETURNING *;

```



delete :

```
DELETE FROM courses
WHERE id = 8;
-- OR 
DELETE FROM courses
WHERE id IN (6,5)
RETURNING *;

```


-------

### REFERENCE

[what is postgres ? ](https://www.postgresqltutorial.com/postgresql-getting-started/what-is-postgresql/)

[varchar vs char ](https://dba.stackexchange.com/questions/126003/index-performance-for-char-vs-varchar-postgres)

[ALTER TABLE](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-update/)

[date type](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-date/)

[ Upsert Using INSERT ON CONFLICT](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-upsert/)


[dvd rental ](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)