create database revisao ;
use revisao;
create table cliente (
    id_cliente INT PRIMARY KEY auto_increment,
    nome_cliente VARCHAR(255),
    cidade_cliente varchar (255) 
    );
    
create table pedidos (
    id_pedidos integer primary key auto_increment,
    quantidade_pedidos integer not null,
    valor_unitario_pedidos decimal (10,5),
    id_cliente integer, 
    foreign key (id_cliente) references cliente(id_cliente)
    );

-- Cadastro de informaçõe 
insert into cliente(nome_cliente,cidade_cliente)values
("Arlindo","Brasil"),
("Felizardo","Russia "),
("Givanni","Usa");

select * from cliente;

insert into pedidos(quantidade_pedidos,valor_unitario_pedidos,id_cliente ) values
(20,15.75,1),
(5,105.99,3),
(4,45,2),
(2,55.89,2),
(1,207.99,3),
(30,300.99,1);

select * from pedidos;


-- visual joiu 
-- mostrar cliente e pedidos 
SELECT
    cliente.nome_cliente,
    pedidos.quantidade_pedidos
FROM cliente
-- uniao 
-- inner join mostrara apenas clientes com pedidos 
JOIN pedidos
ON cliente.id_cliente = pedidos.id_cliente;

-- criando outro visual  nome cliente quantidade e valoor
select 
c.nome_cliente,
p.quantidade_pedidos,
p.valor_unitario_pedidos
from cliente c
join pedidos p on
c.id_cliente=p.id_cliente;

-- quantidade total por cliente

select cliente.nome_cliente, sum(pedidos.quantidade_pedidos) from cliente

-- depois de utizar uma função matemateca , fazer agrupação depoi do join 
join pedidos on cliente.id_cliente = pedidos.id_cliente

group by cliente.nome_cliente  ;

-- criando novos campos 
CREATE VIEW vw_historico_Pedidos AS
SELECT
    cliente.nome_cliente AS 'Nome do Cliente',
    pedidos.quantidade_pedidos AS 'Quantidade Comprada',
    pedidos.valor_unitario_pedidos AS 'Valor Unitário do Pedido',
    pedidos.quantidade_pedidos * pedidos.valor_unitario_pedidos AS 'Total'
FROM cliente
JOIN pedidos
ON cliente.id_cliente = pedidos.id_cliente;
-- salvar consulta 
-- usando view 
select * from vw_historico_Pedidos;


select c.nome_cliente,
count(c.id_cliente) as "Quantidade de Compras",
round(avg(p.quantidade_pedidos*p.valor_unitario_pedidos), 2) as "Tiket Medio",
sum(p.quantidade_pedidos*p.valor_unitario_pedidos)as "Total Gasto"
from cliente c 
join pedidos p on p.id_cliente = c.id_cliente
group by c.nome_cliente;










