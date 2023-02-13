-- User
INSERT INTO "user" (rut,"name",l_name,birthdate,"position",age) 
VALUES
	('11111111','Chato','Mendez','1647-01-23','Secuity',72),
	('222222222','El chavo','del ocho','1980-01-23','Secuity',102);

SELECT * FROM "user" u ;

SELECT u.id AS user_id, concat(u."name", u.l_name) AS f_name,
	p.id as project_id, p."name" ON projects_name, p.date_start, p.date_close
FROM "user" u INNER JOIN project p ON u.id=p.user_id 
WHERE u.rut = '123456789';


-- institution 
INSERT INTO institution ("name",description,address,date_created) 
VALUES
	 ('S.N. Institu','Instite of waster','San nicolas 22, irland, earth','2022-10-12'),
	 ('test','Instite Seek','Kaka 0, El Sol','2022-01-01'),
	 ('Institu Mat','Instite of Salt','Lira 9, Chaucha, Marte','2022-11-01'),
	 ('Institu Seek','Instite Seek','Kaka 0, El Sol','2022-01-01');

SELECT * FROM institutions i ;

SELECT i.id, i."name" as institution_name, i.description, i.address, p.id, p."name" project_name , p.date_start, p.date_close, p.user_id 
FROM "institution" i INNER JOIN project p ON i.id=p.inst_id 
WHERE i.id = 1;


-- Project
INSERT INTO project ("name",date_start,date_close,inst_id,user_id) 
VALUES
	 ('Project 1','2022-01-23','2023-06-03',1,1),
	 ('Project 2','1999-10-22','2023-05-01',2,1);

SELECT * FROM project p;













-- Project
select * from project p;

insert into project ("id", "name", "date_start", "date_close", "user_id")
values(1, "Project 1", "2022-01-23", "2023-06-03", 1);

update project set date_close='2023-04-23' where id=1;

#u.birthdate, u."position", u."age"

select u.id as user_id, concat(u."name", u.l_name) as f_name,
	p.id as project_id, p."name" as projects_name, p.date_start, p.date_close
from "user" u inner join project p on u.id=p.user_id 
where u.rut = '123456789';