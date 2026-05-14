create database generation_brasil;

-- Usar o Bd 
use generation_brasil;

create table cursos(
--
-- Melhor forma e segura de criar um Id Unico 
id_curso varchar(36) default (uuid()) primary key,
titulo_curso varchar(255) not null,
turma varchar(255) not null,
data_inicio date not null
);

alter table cursos
-- add column ----comando para adionar nova coluna
ADD column data_fim date not null  after turma;

alter table cursos
rename column data_inicio to data_inicio_turma;

alter table cursos 
modify column titulo_curso varchar(50) not null;
-- vamos popular os dados 
-- Insert para insserir dados 
insert into cursos (titulo_curso,turma,data_inicio_turma,data_fim)values
('analista de dados', 'gen02', '2026-03-30', '2026-06-28'),
('curso2', 'turma 2', '2026-02-02', '2026-03-03'),
('curso3', 'turma 3', '2026-05-05', '2026-06-06');

SELECT * FROM cursos;

