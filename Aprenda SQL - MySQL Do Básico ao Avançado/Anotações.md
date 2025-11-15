================================ CRIAR BANCO DE DADOS =================================================



CREATE DATABASE db\_nome\_do\_banco\_de\_dados -> Criar o banco de dados

USE db\_nome\_do\_banco\_de\_dados -> acessa o banco de dados











===================================== CRIAR TABELA ====================================================



CREATE TABLE tb\_nome\_da\_tabela(

 	id bigint auto\_increment,

    primeiro\_valor varchar(255),

    segundo\_valor varchar(255),

    terceiro\_valor int,

 

    primary key (id)

);







========================= PRINCIPAIS VALORES PODEM SER ================================================



1\. Números

INT / INTEGER – números inteiros (ex: 1, 200, -50)



FLOAT / DOUBLE / DECIMAL – números com vírgula (ex: 3.14, 100.99)







2\. Texto

CHAR(n) – texto com tamanho fixo (ex: CHAR(2) → 'SP')



VARCHAR(n) – texto com tamanho variável (ex: VARCHAR(100) → nomes, emails)



TEXT – textos longos (ex: descrições)









3\. Datas e Horas

DATE – data (ex: 2025-06-29)



DATETIME – data e hora (ex: 2025-06-29 20:30:00)



TIME – hora (ex: 14:45:00)



YEAR – ano (ex: 2025)











Valores Lógicos

BOOLEAN / TINYINT(1) – verdadeiro ou falso (1 ou 0)











5\. Chaves

PRIMARY KEY – identificador único (geralmente um número)



FOREIGN KEY – referência a outra tabela (por exemplo, city\_id na address vem da city)















NULL → ausência de valor (ex: telefone que não foi informado)



DEFAULT → valor padrão definido no campo (ex: DEFAULT CURRENT\_TIMESTAMP)



AUTO\_INCREMENT → valor que se auto-incrementa (como IDs)







=====================================================================================================================



USE -> Serve para acessar o banco de dados

 	-> Exemplo USE db\_nome\_do\_banco\_de\_dados;



SELECT -> Serve para acessar os valores dentro do banco de dados

 	-> Exemplo SELECT \* FROM tb\_nome\_da\_tabela;

 	 ->  O \* serve para acessar todos os valores dento da tabela escolhida

 	  -> Exemplo para filtra coluna:

 	   -> 1 coluna:

 		SELECT nome\_da\_coluna FROM tb\_nome\_da\_tabela;

 	   -> Para varias colunas deve-se separara os nomes das mesma por "," Exemplo:

 	     -> SELECT nome\_da\_coluna1, nome\_da\_coluna2 FROM tb\_nome\_da\_tabela;

 	-> Com ele é possível efetuar altereções sem gravar no banco

 	   Exemplo SELECT nome\_da\_coluna, nome\_da\_coluna2, nome\_da\_coluna2 - (nome\_da\_coluna2 \* 0.10) FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna <= 10;
Podemos utilizar a palavra reservada AS para dar nome a coluna

 		Exemplo: SELECT nome\_da\_coluna, nome\_da\_coluna2, nome\_da\_coluna2 - (nome\_da\_coluna2 \* 0.10) AS '10% discont' FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna <= 10;





ORDER BY -> Serve para ordenar os resultados da tabela com base nos valores de uma coluna(por exemplo alfabética)

            SELECT nome\_da\_coluna1, nome\_da\_coluna2 FROM tb\_nome\_da\_tabela ORDER BY nome\_da\_coluna1;

 	   -> Utilizando DESC a ordem ficará decrescente

 	      SELECT nome\_da\_coluna1, nome\_da\_coluna2 FROM tb\_nome\_da\_tabela ORDER BY nome\_da\_coluna1 DESC;

 	   -> DICA EXTRA: Podemos ordenar por mais de uma coluna, exemplo

 		SELECT nome, sobrenome FROM pessoas ORDER BY sobrenome, nome;
Isso ordena primeiro pelo sobrenome, e em caso de empates, pelo nome.



 	   -> ASC -> Ascending (Crescente)

 	          ->Ordena os dados do menor para o maior



           -> DESC -> Descending (Decrescente)

 	             ->Ordena os dados do maior para o menor



WHERE -> Filtra registros com base em uma ou mais condições

 	-> Exemplo:
 SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna <= 10;

 	-> Operadores de WHERE



           != ou <> -> Diferente de



 	   < -> Menor que



           <= -> Menor ou igual a que



           > -> Maior que



           >= -> Maior ou igual a que



           = -> Igual que





 

 	  AND -> E

               -> Retorna os valores que atendem a todas as requisições ao mesmo tempo

 

          OR -> Ou

              -> Retorna os valores que atendem pelo menos uma das requisições ao mesmo tempo



          NOT -> Não

               -> Nega a condição, ou seja, retorna os valores que não atendem ao que foi especificado





          IN -> Verifica se um valor está dentro de uma lista de valores especificados, é equivalente a vários OR juntos

               -> Exemplo

 	           SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna IN ('valor1', valor2, valor3);

 	           obs.: para valores do tipo text sempre inserir ente '' ou ""



          BETWEEN -> Utilizado para verificar se um valor está entre dois valores, incluindo os limites, é uma forma prática de fazer uma comparação de intervalo

 		    -> Exemplo

 			SELECT \*  FROM tb\_nome\_da\_tabela  WHERE  nome\_da\_coluna BETWEEN valor1 AND valor2



 	  LIKE -> Usado para fazer buscas por padrões em textos (strings), Permite encontrar valores que contenham, começam com, terminam com ou tenham partes específicas de texto

 		-> Exemplo

 		   SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna LIKE 'A%'

 		   obs.: o % informa que é para trazer os valores que começam com A independente do que venha depois

 			LIKE '%son' → nomes que terminam com "son" (ex: "Jackson")



 			LIKE '%ann%' → nomes que contêm "ann" em qualquer posição (ex: "Joanna")



 			LIKE '\_' → underscore significa qualquer caractere único (ex: LIKE 'A\_' retorna nomes com 2 letras começando com A, como "Al")
Podemos utilizar NOT LIKE também que retorna os valores que não correspondem ao padrão especificado



 	 IS NULL -> Retorna os campos que estão vazios, que não tem informação

 		  -> Exemplo

 			SELECT \* FROM  tb\_nome\_da\_tabela WHERE nome\_da\_coluna IS NULL



 	 LIMIT -> Utilizado para limitar a quantidade de registros retornados por uma consulta, pode ser usado com um valor (quantidade) ou dois valores (ponto de partida e quantidade)

 		-> Exemplo

 		     SELECT \* FROM tb\_nome\_da\_tabela LIMIT 5, 10

 		     obs.: Se você não souber o total de linhas da tabela, pode usar um valor maior no LIMIT sem erro, o banco de dados simplesmente retornará até onde existirem registros





 	 REGEXP -> Regular expression (Expressões regulares)

 		 -> Usado para buscar padrões mais avançados em colunas de texto, é mais poderoso que LIKE, pois permite uso de regras como início, fim, grupos, repetição, etc

 		   -> Exemplos

 			SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna REGEXP 'a'; -> Retorna todos os registros onde nome\_da\_coluna contém a letra "a" em qualquer posição.

 			SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna REGEXP '^a'; -> Retorna registros onde nome\_da\_coluna começa com a letra "a".

 			SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna REGEXP '^a|d'; -> Retorna registros onde nome\_da\_coluna começa com "a" ou contém a letra "d" em qualquer lugar

 			SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna REGEXP '^a|^d'; -> Retorna nomes que começam com "a" ou "d", pois o ^ está aplicado tanto para a quanto para d

 			SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna REGEXP '\[ge]a'; -> Retorna nomes que contêm a letra "g" ou "e" imediatamente antes de "a"

 			SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna REGEXP '^\[ger]a'; -> "^" Indica que a verificação começa desde o início do texto, "\[ger]" Qualquer uma dessas letras: g, e ou r, "a" A segunda letra deve ser 			exatamente "a"

 			Obs.: existem muito mais excreções do REGEXP







HAVING -> Usado para filtrar dados depois do agrupamento (GROUP BY)

 	-> É parecido com o WHERE, mas HAVING age sobre os dados agregados (como COUNT, SUM, AVG, etc.)

 	-> Exemplo:

 	   SELECT nome\_da\_coluna1, COUNT(\*) AS total\_registros FROM tb\_nome\_da\_tabela GROUP BY nome\_da\_coluna1 HAVING total\_registros >= 5;





INNER JOIN -> Utilizado para combinar dados de duas (ou mais) tabelas com base em uma coluna em comum

 	    -> Exemplo

 		SELECT \* FROM tb\_nome\_da\_tabela JOIN tabela2 ON tabela1.coluna\_comum = tabela2.coluna\_comum;

 	    -> Para filtrar diretamente colnas das tabelas utiliza-se assim

 		SELECT tabela1.coluna\_deseja, tabela1.coluna\_deseja, tabela2.coluna\_deseja FROM tabela1 JOIN tabela2 ON tabela1.coluna\_comum = tabela2.coluna\_comum;

 	   -> Exemplo com mais joins

 		SELECT

    		  tb1.coluna\_deseja,

                  tb1.coluna\_deseja,

       		  tb3.coluna\_deseja,

    		  tb2.coluna\_deseja,

    	 	  tb2.coluna\_deseja

 		FROM tabela1 tb1 cus

    		JOIN tabela2 tb12 pay

        		ON tb1.coluna\_comum = tb2.coluna\_comum

    		JOIN tabela3 tb3

        		ON tb1.coluna\_comum = tb3.coluna\_comum



ALIAS -> São "apelidos" para tabelas ou colunas, usados para simplificar o nome nas consultas, facilitam a escrita, especialmente quando se trabalha com várias tabelas ou nomes longos

 	-> Exemplo

 	   SELECT tb1.coluna\_deseja, tb1.coluna\_deseja, tb2.coluna\_deseja FROM tabela1 tb1 JOIN tabela2 tb2 ON tb1.coluna\_comum = tb2.coluna\_comum;



========================================================================= INSERIR DADOS NA TABELA ====================================================================================================================





INSERT INTO -> Utilizado para inserir dados em uma tabela

 	     -> É necessário informar os valores na mesma ordem das colunas (ou especificar quais colunas serão preenchidas)

 	     -> Exemplo

 		INSERT INTO tb\_nome\_da\_tabela VALUES (DEFAULT, 'Valor 1', 'Valor 2')

 		obs.: Quando a tabela possui uma coluna com AUTO\_INCREMENT, pode-se usar DEFAULT ou omitir o valor dessa coluna.

 		Caso haja valores que não são obrigatórios e você só queira adicionar um valor segue oe exemplo

 		INSERT INTO tb\_nome\_da\_tabela (nome\_do\_campo) VALUES ('Valor do campo')

 	     -> Para inserir mais de uma linha é só inserir o () com os valores quantas vezes necessárias

 		-> Exemplo

 		  INSERT INTO tb\_nome\_da\_tabela VALUES (DEFAULT, 'Valor 1', 'Valor 2'), (DEFAULT, 'Valor 1', 'Valor 2'), (DEFAULT, 'Valor 1', 'Valor 2')

 	     -> Para inserir duas tabelas relacionadas

 		-> Exemplo:

 		  INSERT INTO tb\_nome\_da\_tabela

 		  VALUES (DEFAULT, 'Valor 1', 'Valor 2');



 		  INSERT INTO tb\_nome\_da\_tabela2

 		  VALUES (DEFAULT, 'Valor 1', last\_insert\_id(), 'Valor 2')



last\_insert\_id() -> Função que retorna o último valor AUTO\_INCREMENT gerado na sessão atual

 		  -> Só funciona corretamente se a tabela anterior tiver uma coluna AUTO\_INCREMENT







============================================================================= COPIAR TABELAS =============================================================================================================================





CREATE TABLE ... AS SELECT -> Utilizado para criar uma nova tabela com base na estrutura e/ou dados de outra tabela.

 			     -> Exemplo de como criar tabela copiando todos os dados da original

 				CREATE TABLE  tb\_nome\_da\_nova\_tabela AS SELECT \* from  tb\_nome\_da\_tabela

 			     -> Exemplo de como criar tabela copiando apenas a estrutura (sem dados)

 				CREATE TABLE tb\_nome\_da\_nova\_tabela AS SELECT \* FROM tb\_nome\_da\_tabela WHERE 1 = 0;

 			     -> Exemplo de como criar tabela copiando colunas específicas e com filtro

 				CREATE TABLE tb\_nome\_da\_nova\_tabela AS SELECT coluna1, coluna2 FROM tb\_nome\_da\_tabela;





============================================================================= ATUALIZANDODA DADOS DAS TABELAS =============================================================================================================================



UPDATE -> Utilizado para atualizar (alterar) valores existentes em uma tabela

 	-> Exemplo:

 	   UPDATE tb\_nome\_da\_tabela SET nome\_da\_coluna = 'valor desejado' WHERE identificador\_da\_linha = 1;

 	obs.: UPDATE → Informa qual tabela será atualizada



 	      SET → Define qual coluna receberá o novo valor



 	      WHERE → Indica qual linha será modificada (sem WHERE, todas as linhas da tabela são alteradas)



DELETE -> Utilizado para deletar valores existentes em uma tabela

 	-> Exemplo:

 	  DELETE FROM tb\_nome\_da\_tabela WHERE identificador\_da\_linha = 10;







============================================================================= REMOVER TABELAS =============================================================================================================================







DROP TABLE -> Exclui a tabela

 	   -> Exemplo

 	      DROP TABLE tb\_nome\_da\_tabela





TRUNCATE TABLE -> Remove os dados contidos na tabela

 	       -> Exemplo

 	         TRUNCATE TABLE tb\_nome\_da\_tabela







================================================================================ FUNÇÕES SQL ===============================================================================================================================





Documentação: https://www.w3schools.com/sql/sql\_ref\_sqlserver.asp





Sempre seguirá a seguinte sintaxe nome\_da\_funcao()



Algumas funções





                         Funções de Agregação (Agrupamento de Dados)



Função	               O que faz	                                   Exemplo

COUNT()	       Conta quantos registros existem	            SELECT COUNT(\*) FROM tb\_nome\_da\_tabela;

SUM()	       Soma os valores de uma coluna numérica	    SELECT SUM(preco) FROM vendas;

AVG()	       Calcula a média dos valores	            SELECT AVG(nota) FROM alunos;

MAX()	       Retorna o maior valor	                    SELECT MAX(salario) FROM funcionarios;

MIN()	       Retorna o menor valor	                    SELECT MIN(idade) FROM pessoas;





                        Funções de Texto (Strings)



Função	                     O que faz	                                             Exemplo

UPPER()	             Converte texto para maiúsculas	                 SELECT UPPER(nome) FROM clientes;

LOWER()	             Converte texto para minúsculas	                 SELECT LOWER(nome) FROM clientes;

LENGTH()	     Retorna o número de caracteres	                 SELECT LENGTH(nome) FROM clientes;

CONCAT()	     Junta (concatena) dois ou mais textos	         SELECT CONCAT(nome, ' ', sobrenome) FROM clientes;

SUBSTRING()	     Retorna parte do texto	                         SELECT SUBSTRING(nome, 1, 3) FROM clientes; → Primeiras 3 letras

REPLACE()	     Substitui partes do texto	                         SELECT REPLACE(nome, 'a', '@') FROM clientes;

TRIM()	             Remove espaços em branco nas extremidades	         SELECT TRIM(' teste '); → teste







 			Funções de Data e Hora





Função	                      O que faz	                                       Exemplo

NOW()	              Retorna a data e hora atuais	              SELECT NOW();

CURDATE()	      Retorna apenas a data atual	              SELECT CURDATE();

CURTIME()	      Retorna apenas a hora atual	              SELECT CURTIME();

YEAR()	              Extrai o ano	                              SELECT YEAR(data\_nascimento) FROM clientes;

MONTH()	              Extrai o mês	                              SELECT MONTH(data\_nascimento) FROM clientes;

DAY()	              Extrai o dia	                              SELECT DAY(data\_nascimento) FROM clientes;

DATEDIFF()	      Diferença de dias entre duas datas	      SELECT DATEDIFF(CURDATE(), data\_nascimento) FROM clientes;





 			Funções Condicionais



Função	                                                                O que faz	                                          Exemplo

IF(condição, valor\_se\_verdadeiro, valor\_se\_falso)    Retorna um valor dependendo da condição	          SELECT IF(idade >= 18, 'Maior', 'Menor') FROM clientes;

CASE	                                             Cria múltiplas condições (como if/else)	          SELECT nome CASE WHEN idade < 12 THEN 'Criança' WHEN idade < 18 THEN Adolescente' ELSE 'Adulto' END AS classificação FROM pessoas;





============================================================================================= SUB QUERY ====================================================================================================================================





SUB QUERY -> É uma consulta dentro de outra consulta

 	  -> Usada quando você precisa de um valor calculado dinamicamente por outra SELECT

 	  -> Pode ser usada em cláusulas como WHERE, FROM, SELECT, HAVING, etc.

 	   -> Exemplo:

 		SELECT \* FROM tb\_nome\_da\_tabela WHERE nome\_da\_coluna > (SELECT nome\_da\_funcao(nome\_da\_coluna) FROM tb\_nome\_da\_tabela)

 		obs.: A subquery é tudo que está entre parênteses, e não apenas o que está após o







=============================================================================================== VIEW ======================================================================================================================================







VIEW -> Uma VIEW é uma tabela virtual criada a partir de uma consulta SQL, ou seja um "atalho", funciona como um nome que representa uma consulta complexa, facilitando o reuso

 	-> Exemplo:

 	  CREATE VIEW nome\_da\_view AS

 	  SELECT

 	  	tb1.coluna\_deseja,

          	tb1.coluna\_deseja,

          	tb2.coluna\_deseja,

    	  	tb2.coluna\_deseja

 	  FROM tb\_nome\_da\_nova\_tabel tb1

 	  JOIN tb\_nome\_da\_nova\_tabel tb2

 	  ON tb1.coluna\_comum = tb2.coluna\_comum



 	 -> É possível localizado dentro do banco de dados em VIEW

 	 -> para alterar a VIEW coloque CREATE OR REPLACE VIEW, para alterar caso já exista uma VIEW de mesmo nome

 	 -> Recomento criar VIEW como CREATE OR REPLACE VIEW

 	  -> Exemplo

 	      CREATE OR REPLACE VIEW nome\_da\_view AS

 	      SELECT

 	  	tb1.coluna\_deseja,

          	tb1.coluna\_deseja,

          	tb2.coluna\_deseja,

    	  	tb2.coluna\_deseja

 	      FROM tb\_nome\_da\_nova\_tabel tb1

 	      JOIN tb\_nome\_da\_nova\_tabel tb2

 	      ON tb1.coluna\_comum = tb2.coluna\_comum







ALTER TABLE -> É usado para modificar a estrutura de uma tabela existente

&nbsp;	     -> ADD -> Adiciona uma nova  coluna
		-> Exemplo

&nbsp;		   ALTER TABLE nome\_da\_tabela ADD nome\_da\_nova\_coluna

&nbsp;	     -> DROP COLUMN - Remove uma coluna já existente 

 		-> Exemplo

 		   ALTER TABLE nome\_da\_tabela DROP COLUMN nome\_da\_coluna

 	     -> MODIFY - Altera o tipo de um coluna já existente

 		-> Exemplo

 		   ALTER TABLE nome\_da\_tabela MODIFY nome\_da\_coluna novo\_tipo;

&nbsp;		   OBS.: Em alguns bancos a sintase e diferente 

&nbsp;			ALTER TABLE nome\_da\_tabela ALTER COLUMN nome\_da\_coluna TYPE novo\_tipo;

 	     -> RENAME - Altera o nome de uma tabela já existente

 		-> Exemplo

 		   RENAME TABLE nome\_antigo TO nome\_novo;

 	     -> RENAME COLUMN  - Altera o nome de uma coluna já existente

 		-> Exemplo

 		   ALTER TABLE nome\_da\_tabela RENAME COLUMN nome\_antigo TO nome\_novo;







&nbsp;FOREIGN KEY -> Chave estrangeira

&nbsp;	      -> Utilizada para criar um vínculo entre duas tabelas. Ela garante que o valor em uma coluna exista como chave primária em outra tabela 

&nbsp;	       -> Exemplo 

&nbsp;		  FOREIGN KEY (nome\_da\_coluna) REFERENCES nome\_da\_outra\_tabela(nome\_da\_coluna)



























============================================ OPERADORES MATEMATICOS =========================================================================



 	+ -> Soma



 	- -> Subtrai



 	\* -> Multiplica



 	/ -> Divide



 	Só podem ser utilizados em colunas do tipo numérico





============================================ OPERADORES DE COMPARAÇÃO =========================================================================



           != ou <> -> Diferente de



 	   < -> Menor que



           <= -> Menor ou igual a que



           > -> Maior que



           >= -> Maior ou igual a que



           = -> Igual que





============================================ OPERADORES LÓGICOS =========================================================================



 	   AND -> E

                -> Retorna os valores que atendem a todas as requisições ao mesmo tempo

 

           OR -> Ou

               -> Retorna os valores que atendem pelo menos uma das requisições ao mesmo tempo



           NOT -> Não

                -> Nega a condição, ou seja, retorna os valores que não atendem ao que foi especificado

