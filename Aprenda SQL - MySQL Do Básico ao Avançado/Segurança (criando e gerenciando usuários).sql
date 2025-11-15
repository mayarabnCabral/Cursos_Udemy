USE mysql;

SELECT * FROM user; -- Verificar usuários cadastrados ( posso utilizar também SELECT * FROM nome_do_banco.user)

-- Criando usuários (INICIO)

    -- Como criar o usuário 
        CREATE USER ana IDENTIFIED BY '1212'; -- Estamos criando o novo usuário com a sua senha  
              -- quando temos no campo HOST o sinal de % significa que não tem restrições de local de acesso (como não especificados ela pode acessar de qualquer local)

        CREATE USER joao@localhost IDENTIFIED BY '1212'; -- Aqui estamos especificando de qual local o usuário pode acessar o banco de dados (Podemos utilizar o ip também {Exemplo joao@127.0.0.1})

        CREATE USER priscila@dominioDaEmpresa.com IDENTIFIED BY '1212'; -- Aqui estamos restringindo o acesso para apenas computadores que estão dentro do dominio da empresa (Podemos utilizar o ipdo computador também {Exemplo priscila@192.168.10.1})



-- Criando usuários (FIM)

-- Removendo Usuários (INICIO)

    -- Como criar o remover 
        DROP USER priscila@dominioDaEmpresa.com; -- Um erro comum é informar apenas o nome (nesse caso priscila), mas devemos informar o usuário completo com o host (nesse caso priscila@dominioDaEmpresa.com)
        DROP USER joao@localhost;
        DROP USER ana;
-- Removendo Usuários (FIM)

-- ALterar senha de usuário (INICIO)

    -- No popSQL
        SET PASSWORD FOR joao@localhost = '4444'; -- Para alterar a senha do usuário que você está logada é só digitar SET PASSWORD = 'nova_senha'
    
    -- No workbench
    /* Siga por Administration > Users and Privileges > Selecione o usuário > No campo Password digite a nova senha > Apply ou clicando no botão Expire password (nessa opção o usuário devera digitar ma nova senha no proximo acesso )*/

-- ALterar senha de usuário (FIM)

-- Aplicando privilegios de usuário (INICIO)
    -- Quando criamos um usuário ele não é criado com nenhuma permissão

    -- Para verificar permissões de um usuário 
         SHOW GRANTS FOR ana;

    -- Consedendo permissões 
        GRANT SELECT, INSERT, UPDATE, DELETE ON sakila.* TO ana; -- Aqui estamos consedendo ao usuário (no caso o usuário ana), a permissão de utilizar o de leitura, inserção, edição e exclusão no banco de dados sakila

-- Aplicando privilegios de usuário (FIM)

-- Removendo privilegios de usuário (INICIO)

    -- Para remover privilegios
        REVOKE UPDATE ON sakila.* FROM ana

-- Removendo privilegios de usuário (FIM)


-- Criando Usuário ADM (INICIO)

    -- Para um banco de dados 
        GRANT ALL ON sakila.* TO ana; -- Aqui estamos consedendo ao usuário (no caso o usuário ana), todas as permissões no banco de dados sakila

    -- Para todos os bancos de dados 
        GRANT ALL ON *.* TO joao@localhost; -- Aqui estamos consedendo ao usuário (no caso o usuário joao), todas as permissões em todos os bancos de dados
        SHOW GRANTS FOR joao@localhost; -- Verificar os previlégios

-- Criando Usuário ADM (FIM)




-- TESTES

    CREATE USER priscila IDENTIFIED BY '1212';

    SHOW GRANTS FOR priscila;

    GRANT SELECT, INSERT, UPDATE ON SAKILA.* TO priscila;
    -- Retorno GRANT SELECT, INSERT, UPDATE ON `sakila`.* TO `priscila`@`%`

    REVOKE UPDATE ON sakila.* FROM priscila
    -- Retorno GRANT SELECT, INSERT ON `sakila`.* TO `priscila`@`%`