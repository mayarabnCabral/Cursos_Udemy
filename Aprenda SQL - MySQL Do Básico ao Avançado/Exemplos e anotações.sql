USE SAKILA
-- SELECT actor_id, first_name, last_name FROM actor WHERE actor_id <= 10 ORDER BY last_name DESC, first_name DESC;


-- SELECT customer_id, amount, amount - (amount * 0.10) AS '10% discont' FROM payment WHERE customer_id = 1;

-- SELECT * FROM payment WHERE amount != 0.99;


-- SELECT * FROM  address WHERE district = 'Texas'

-- SELECT * FROM customer WHERE store_id = 1 AND active = 1 AND customer_id < 10;

-- SELECT * FROM payment WHERE staff_id = 1 OR amount = 0.99;

-- SELECT * FROM payment WHERE NOT staff_id = 1 AND amount = 0.99;


-- SELECT * FROM address WHERE district IN ('Alberta', 'Texas', 'California');

-- SELECT * FROM actor WHERE first_name LIKE 'A%';
-- SELECT * FROM actor WHERE first_name LIKE '%C';
-- SELECT * FROM actor WHERE first_name LIKE '%A%';
-- SELECT * FROM actor WHERE first_name LIKE '_rac_';

-- SELECT * FROM address WHERE address2 IS NULL;

-- SELECT * FROM actor LIMIT 5, 10;

-- SELECT * FROM actor WHERE first_name REGEXP 'a';
-- SELECT * FROM actor WHERE first_name REGEXP '^a';
-- SELECT * FROM actor WHERE first_name REGEXP '^a|d';
-- SELECT * FROM actor WHERE first_name REGEXP '^a|^d';
-- SELECT * FROM actor WHERE first_name REGEXP '[ge]a';
-- SELECT * FROM actor WHERE first_name REGEXP '^[ger]a';

-- SELECT * FROM customer JOIN payment ON customer.customer_id = payment.payment_id;

-- SELECT customer.customer_id, customer.first_name, customer.last_name, payment.rental_id, payment.amount FROM customer JOIN payment ON customer.customer_id = payment.payment_id;
--SELECT 
--    cus.customer_id, 
--    cus.first_name, 
--    cus.last_name, 
--    adr.address,
--    pay.rental_id, 
--    pay.amount
--FROM customer cus 
--    JOIN payment pay 
--        ON cus.customer_id = pay.payment_id 
--    JOIN address adr 
--        ON cus.customer_id = adr.address_id

-- SELECT cus.customer_id, cus.first_name, cus.last_name, pay.rental_id, pay.amount FROM customer cus JOIN payment pay ON cus.customer_id = pay.payment_id;

-- INSERT INTO language
-- VALUES (DEFAULT, 'Portuguese', '2025-06-30 05:02:19')

-- INSERT INTO language
-- VALUES  (DEFAULT, 'Portuguese', '2025-06-30 05:02:19'),
--		(DEFAULT, 'Spanish', '2024-06-30 05:02:19'),
--		(DEFAULT, 'Polish', '2023-06-30 05:02:19')


-- INSERT INTO country 
-- VALUES (DEFAULT, 'Guiana Brasileira', '2036-02-15 04:44:00');

-- INSERT INTO city 
-- VALUES (DEFAULT, 'Pernambuco em pé', last_insert_id(), '2034-02-15 04:44:00')

-- CREATE TABLE payment_backup AS SELECT * from payment;
-- CREATE TABLE payment_estrutura AS SELECT * FROM payment WHERE 1 = 0;
-- CREATE TABLE payment_algumas_colunas AS SELECT payment_id, customer_id, amount FROM payment;


-- TRUNCATE TABLE payment_backup
-- DROP TABLE payment_backup

-- UPDATE payment SET amount = 15.99 WHERE payment_id = 1;

-- DELETE FROM payment WHERE payment_id = 5003;


-- SELECT  MAX(amount) FROM payment 
-- SELECT  MAX(amount), MIN(amount), AVG(amount) FROM payment 
-- SELECT  MAX(amount) AS Maior, MIN(amount) AS Menor, AVG(amount) AS 'Média de valores' FROM payment 
-- SELECT  MAX(amount) AS Maior, MIN(amount) AS Menor, AVG(amount) AS 'Média de valores', SUM(amount) 'Total de vendas', COUNT(amount) 'Vendas feitas' FROM payment WHERE staff_id = 2
-- SELECT customer_id, SUM(amount) AS Total FROM payment GROUP BY customer_id ORDER BY total DESC


-- SELECT 
	---cus.customer_id AS ID,
    -- cus.first_name AS Nome,
    -- cus.last_name AS Sobrenome,
    -- SUM(amount) AS Total 
-- FROM payment pay 
-- JOIN customer cus USING(customer_id) 
-- GROUP BY customer_id ORDER BY total DESC


-- SELECT 
	--cus.customer_id AS ID,
    -- cus.first_name AS Nome,
    -- cus.last_name AS Sobrenome,
    -- SUM(amount) AS Total,
    -- COUNT(amount) AS Compras 
-- FROM payment pay 
-- JOIN customer cus USING(customer_id) 
-- GROUP BY customer_id 
-- HAVING Total >= 150 AND Compras >= 35
-- ORDER BY total DESC


-- SELECT * 
-- FROM payment
-- WHERE amount > (SELECT AVG(amount) FROM payment)


-- SELECT * 
-- FROM payment
-- WHERE amount = (
   -- SELECT MAX(amount) 
    --FROM payment 
    -- WHERE customer_id = 1
   -- )

-- SELECT *
-- FROM customer
-- WHERE customer_id IN (
-- SELECT customer_id
-- FROM payment 
-- GROUP BY customer_id
-- HAVING COUNT(*) > 35
-- )


-- SELECT *
-- FROM customer
-- WHERE customer_id IN (
-- SELECT customer_id
-- FROM payment 
-- GROUP BY customer_id
-- HAVING COUNT(*) > 35
-- )


-- CREATE OR REPLACE VIEW vendas_por_cliente AS 
-- SELECT 
-- cus.customer_id,
-- cus.first_name,
-- cus.last_name,
-- pay.amount
-- FROM customer cus
-- JOIN payment pay
	-- ON cus.customer_id = pay.payment_id
-- ORDER BY pay.amount ASC



-- SELECT TRIM('    Carros    '); -- Remove os espações
-- SELECT LTRIM('    Carros    '); -- Remone os espações da esquerda
-- SELECT RTRIM('    Carros    '); -- Remove os espações da direita
-- SELECT TRIM(BOTH 'a' FROM 'aaaaCarrosaaaa') -- Remove as letras repeditas do começo ou fim 
-- SELECT TRIM(LEADING 'a' FROM 'aaaaCarrosaaaa') -- Remove as letras repeditas apenas do começo
-- SELECT TRIM(TRAILING 'a' FROM 'aaaaCarrosaaaa') -- Remove as letras repeditas apenas do fim


-- SELECT LOCATE('Carros') -- Localiza a posição de uma letra 

-- SELECT LCASE('Carros') -- Alterar todas as letras para minusculo
-- SELECT UCASE('Carros') -- Alterar todas as letras para maiusculo

-- SELECT REPEAT('Carros', 5) -- Repete a palavra quantas vezes for informado

-- SELECT LEFT('Carros', 3);  -- Informa as primeiras letras na quantidade informada
-- SELECT RIGHT('Carros', 3); -- Informa as últimas letras na quantidade informada
