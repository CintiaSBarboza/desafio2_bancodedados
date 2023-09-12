import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# 1) Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).
result = cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2) Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.
result = cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Cíntia", 41, "Python"), (2, "Sonia", 26, "Engenharia"), (3, "Maria", 18, "Dados"), (4, "Silvio", 34, "Dados"), (5, "Pablo", 29, "Engenharia")')

# 3) Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
result = cursor.execute('SELECT * FROM alunos')

# b)  Selecionar o nome e a idade dos alunos com mais de 20 anos.
result = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
result = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" order by nome')

# d) Contar o número total de alunos na tabela.
result = cursor.execute('SELECT COUNT(*) from alunos')

#4) Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
result = cursor.execute('UPDATE alunos set idade = 28 WHERE id = 1')

#b) Remova um aluno pelo seu ID.
result = cursor.execute('DELETE FROM alunos WHERE id = 1')
result = cursor.execute('SELECT * FROM alunos')

for item in result:
  print(item)

conexao.commit()
conexao.close

#5) Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). 
result = cursor.execute('CREATE TABLE clientes(id INT primary key, nome VARCHAR(100), idade INT, saldo float);')

#Insira alguns registros de clientes na tabela.
result = cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Cíntia", 41, 1000), (2, "Sonia", 26, 200), (3, "Maria", 18, 500), (4, "Silvio", 34, 1200), (5, "Pablo", 29, 300)')
result = cursor.execute('SELECT * FROM clientes')

#6) Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
result = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

#b) Calcule o saldo médio dos clientes.
result = cursor.execute('SELECT AVG(saldo) FROM clientes')

#c) Encontre o cliente com o saldo máximo.
result = cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')

#d) Conte quantos clientes têm saldo acima de 1000.
result = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')

#7) Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
result = cursor.execute('UPDATE clientes set saldo = 1500 WHERE id = 1')
result = cursor.execute('SELECT * FROM clientes')

#b) Remova um cliente pelo seu ID.
result = cursor.execute('DELETE FROM clientes WHERE id = 4')
result = cursor.execute('SELECT * FROM clientes')

for item in result:
  print(item)

conexao.commit()
conexao.close

#8) Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id 
# (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).
result = cursor.execute('CREATE TABLE compras(id INT primary key, cliente_id INT, produto VARCHAR(100), valor float, CONSTRAINT fk_clientes FOREIGN KEY(cliente_id) REFERENCES clientes (id));')

# Insira algumas compras associadas a clientes existentes na tabela "clientes".
result = cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "caderno", 20), (2, 1, "caneta", 2.20), (3, 2, "caderno", 24)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra.
result = cursor.execute('SELECT c.nome, co.produto, co.valor FROM compras as co INNER JOIN clientes as c on c.id = co.cliente_id')
result = cursor.execute('SELECT * FROM compras')

for item in result:
  print(item)

conexao.commit()
conexao.close




