import sqlite3

conexao = sqlite3.connect('escola')
cursor = conexao.cursor()

#1.Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(250), idade INT, curso VARCHAR(250));')

#2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1, "Lady Gaga", 37, "Python básico")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2, "Beyonce", 42, "Java básico")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3, "Britney Spears", 41, "JavaScript básico")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4, "Adele", 35, "Django básico")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5, "Katy Perry", 38, "Python Avançado")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6, "Billie Eilish", 21, "Python básico")')

#3. Consultas Básicas Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
    print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome FROM alunos WHERE idade > 20')
for alunos in dados:
    print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Python básico" ORDER BY nome')
for alunos in dados:
    print(alunos)

#d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in dados:
    print(alunos) 

#4.Atualização e Remoção 
#a) Atualize a idade de um aluno específico na tabela. 
cursor.execute('UPDATE alunos SET idade=43 WHERE nome="Beyonce"')

#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos where id=1')

#5.Criar uma Tabela e Inserir Dados - Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
cursor.execute('CREATE TABLE clientes(id INT primary key, nome VARCHAR(250), idade INT, saldo FLOAT);')

#Insira alguns registros de clientes na tabela
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1, "Conceição Evaristo", 76, 10000000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2, "Carolina Maria de Jesus", 62, 90000000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3, "Clarice Lispector", 57, 870000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4, "Rachel de Queirozc", 93, 97000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5, "Karina Buhr", 49, 7000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(6, "Lygia Fagundes Telles", 103, 400)')


cursor.execute('UPDATE clientes SET nome="Rachel de Queiroz" WHERE nome="Rachel de Queirozc"')


#6.Consultas e Funções Agregadas Escreva consultas SQL para realizar as seguintes tarefas:
#a)Selecione o nome e a idade dos clientes com idade superior a 50 anos.
infos = cursor.execute('SELECT nome, idade FROM clientes WHERE idade >= 50')
for clientes in infos:
    print(clientes)

#b)Calcule o saldo médio dos clientes.
infos = cursor.execute('SELECT AVG(saldo) FROM clientes')
for clientes in infos:
    print(clientes) 

#c)Encontre o cliente com o saldo máximo.
infos = cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX (saldo) FROM clientes)')
for clientes in infos:
    print(clientes)  

#d)Conte quantos clientes têm saldo acima de 10000.
infos = cursor.execute('SELECT COUNT (*) FROM clientes WHERE saldo >= 10000')
for clientes in infos:
    print(clientes)   

#7.Atualização e Remoção com Condições 
#a)Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 880000 WHERE id=2')
cursor.execute('UPDATE clientes SET saldo = 100000 WHERE id=1')

#b)Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id=3')

#8.Junção de Tabelas. Crie uma segunda tabela chamada "compras" com os campos: id(chave primária),cliente_id(chave estrangeira referenciando o id da tabela"clientes"),produto(texto) e valor(real).
cursor.execute('CREATE TABLE compras(id INT primary key, cliente_id INT, produto VARCHAR(250), valor FLOAT, CONSTRAINT fk_clientes FOREIGN KEY(cliente_id) REFERENCES clientes (id))')

#Insira algumas compras associadas a clientes existentes na tabela "clientes".
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(1, 1, "Lápis", 80.0), (2, 2, "Caderno", 100), (3, 5, "Caneta", 150), (4, 1, "Livro", 800)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
infos = cursor.execute('SELECT c.nome, co.produto, co.valor FROM compras as co inner join clientes as c on c.id = co.cliente_id')

for item in infos:
    print(item)

conexao.commit()
conexao.close()