CREATE DATABASE carros_locadora;
USE carros_locadora;


-- Criando tabelsa Marcas (INICIO)

CREATE TABLE marcas (
	marcas_id INT NOT NULL AUTO_INCREMENT,
    nome_marca VARCHAR(255) NOT NULL,
    PRIMARY KEY (marcas_id)
);

-- Criando tabelsa Marcas (FIM)*/

-- Alterado tabelsa Marcas (INICIO)

ALTER TABLE marcas ADD origem VARCHAR(255);
ALTER TABLE marcas RENAME COLUMN marcas_id TO id;
ALTER TABLE marcas RENAME COLUMN nome_marca TO nome;
-- Criando tabelsa Marcas (FIM)

-- Criando tabelsa Inventário (INICIO)

CREATE TABLE inventario (
	id INT NOT NULL AUTO_INCREMENT,
    modelo VARCHAR(255) NOT NULL,
    ano INT NOT NULL,
    transmissao VARCHAR(255) NOT NULL,
    motor VARCHAR(255) NOT NULL,
    combustivel VARCHAR(255) NOT NULL,
    marcas_id INT NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (marcas_id) REFERENCES marcas(id)
);

-- Criando tabelsa Inventário (FIM)

-- Criando tabelsa Clientes (INICIO)

CREATE TABLE clientes (
	id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255)  NOT NULL,
    PRIMARY KEY (id)
);

-- Criando tabelsa Clientes (FIM)

-- Criando tabelsa PAgamentos (INICIO)

CREATE TABLE pagamentos (
	id INT NOT NULL AUTO_INCREMENT,
    clientes_id INT NOT NULL,
    valor FLOAT NOT NULL,
    tipo_de_pagamento VARCHAR(255)  NOT NULL,
    pago BOOLEAN NOT NULL,
    data_pagamento DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (clientes_id) REFERENCES clientes(id)
);

ALTER TABLE pagamentos ADD inventario_id INT NOT NULL;
ALTER TABLE pagamentos ADD CONSTRAINT fk_inventario FOREIGN KEY (inventario_id) REFERENCES inventario(id);

-- Criando tabelsa Pagamentos (FIM)

-- Inserindo dados nas tabelas (INICIO)

	-- Tabela Marcas  (INICIO)
		INSERT INTO marcas (nome, origem)
        VALUES 
         ('Chevrolet', 'EUA'),
         ('Honda', 'Japão'),
         ('Fiat','Italia'),
         ('Renault', 'França'),
         ('Nissan', 'Japão'),
         ('Toyota', 'Japão'),
         ('Volvo', 'Suécia'),
         ('Ford', 'EUA'),
         ('Dodge', 'EUA'), 
         ('Volkswagen', 'Alemanha'),
         ('Porsche', 'Alemanha'),
         ('Mercedes-Benz', 'Alemanha'),
         ('Alfa Romeo','Italia'),
         ('Harley-Davidson','EUA'),
         ('Royal Enfield','Índia'),
         ('Yamaha','Japão'),
         ('Ferrari', 'Itália'),
		 ('Bugatti', 'França'),
		 ('McLaren', 'Reino Unido'),
         ('Lamborghini', 'Itália');
         
    -- Tabela Marcas  (FIM)
    
    -- Tabela Intentário  (INICIO)
		INSERT INTO inventario (modelo, ano, transmissao, motor, combustivel, marcas_id)
        VALUES 
			('Chevrolet Corvette', 1960, 'Manual 4 marchas', 'V8 4.6L', 'Gasolina', 1),
			('Honda Civic Touring', 2022, 'CVT automática', '1.5L Turbo', 'Gasolina', 2),
			('Fiat Toro Volcano', 2023, 'Automática de 9 marchas', '2.0L Turbo Diesel', 'Diesel', 3),
			('Renault Captur Intense', 2021, 'CVT automática', '1.3L Turbo', 'Flex', 4),
			('Nissan Sentra Advance', 2022, 'CVT automática', '2.0L 16V', 'Gasolina', 5),
			('Toyota Corolla Altis Hybrid', 2023, 'CVT automática', '1.8L Híbrido', 'Híbrido (Gasolina/Elétrico)', 6),
			('Volvo XC60 Recharge', 2023, 'Automática de 8 marchas', '2.0L Turbo Híbrido', 'Híbrido Plug-in', 7),
			('Ford Mustang GT', 2020, 'Automática de 10 marchas', '5.0L V8', 'Gasolina', 8),
			('Dodge Charger R/T', 1970, 'Manual 4 marchas', '7.2L V8 (440 Magnum)', 'Gasolina', 9),
			('Volkswagen Golf GTI', 2022, 'Automática DSG de 7 marchas', '2.0L Turbo', 'Gasolina', 10),
			('Porsche 911 Carrera S', 2023, 'Automática PDK de 8 marchas', '3.0L Boxer Biturbo', 'Gasolina', 11),
			('Mercedes-Benz C 300 AMG', 2022, 'Automática de 9 marchas', '2.0L Turbo Híbrido leve', 'Gasolina', 12),
			('Alfa Romeo Giulia Quadrifoglio', 2023, 'Automática de 8 marchas', '2.9L V6 Biturbo', 'Gasolina', 13),
			('Harley-Davidson Street Glide Special', 2021, '6 marchas', 'Milwaukee-Eight 114 (1868cc)', 'Gasolina', 14),
			('Royal Enfield Meteor 350', 2023, '5 marchas', '349cc monocilíndrico', 'Gasolina', 15),
			('Yamaha MT-09 SP', 2022, '6 marchas', '889cc 3 cilindros', 'Gasolina', 16),
			('Ferrari 250 GTO', 1962, 'Manual 5 marchas', '3.0L V12', 'Gasolina', 17), 
			('Bugatti Type 57SC Atlantic', 1938, 'Manual 4 marchas', '3.3L Inline-8', 'Gasolina', 18),
			('McLaren F1', 1994, 'Manual 6 marchas', '6.1L V12 (BMW)', 'Gasolina', 19),
			('Lamborghini Miura SV', 1971, 'Manual 5 marchas', '4.0L V12', 'Gasolina', 20),
			('Porsche 959', 1986, 'Manual 6 marchas', '2.8L Flat-6 Biturbo', 'Gasolina', 11),
			('Mercedes-Benz 300SL Gullwing', 1955, 'Manual 4 marchas', '3.0L Inline-6', 'Gasolina', 12),
			('Dodge Challenger Demon', 2018, 'Automática de 8 marchas', '6.2L V8 Supercharged', 'Gasolina', 9),
			('Toyota 2000GT', 1967, 'Manual 5 marchas', '2.0L Inline-6', 'Gasolina', 6),
			('Nissan Skyline GT-R R34 V-Spec II', 2002, 'Manual 6 marchas', '2.6L Twin-Turbo I6', 'Gasolina', 5),
			('Honda NSX (1ª geração)', 1991, 'Manual 5 marchas', '3.0L V6 VTEC', 'Gasolina', 2);
    -- Tabela Intentário  (FIM)
    
	-- Tabela Clientes  (INICIO)
		
        INSERT INTO clientes (nome,sobrenome,endereco)
        VALUES 
			('Andre', 'Iacono', 'Rua 1'),
			('Mayara', 'Bueno Nunes Cabral', 'Rua 5'),
            ('Telma', 'Bueno', 'Rua 2'),
            ('Marina', 'Bueno Nunes Cabral', 'Rua 3'),
            ('Mariana', 'Bueno Nunes Cabral', 'Rua 4'),
			('Carlos', 'Silva', 'Rua 6'),
			('Fernanda', 'Souza', 'Rua 7'),
			('Lucas', 'Pereira', 'Rua 8'),
			('Renata', 'Costa', 'Rua 9'),
			('João', 'Almeida', 'Rua 10');
    -- Tabela Clientes  (FIM)
    
	-- Tabela Pagamentos  (INICIO)
		INSERT INTO pagamentos (clientes_id, valor, tipo_de_pagamento, pago, data_pagamento, inventario_id)
        VALUES 
		 (1, 145.000, NULL, 0 ,NULL, 21),
         (2, 30.000, 'Pix', 1 , '2025-06-01 14:30:00', 27),
         (2, 330.000, 'Pix', 1 , '2025-06-05 12:35:29', 1),
         (3, 22000, 'Boleto', 1, '2025-06-02 11:00:00', 3),
		 (4, 28000, 'Cartão de debito', 1, '2025-06-03 15:45:00', 4),
         (5, 26000, 'Dinheiro', 1, '2025-06-04 09:20:00', 5),
		 (6, 18000, NULL, 0, NULL, 6),
         (7, 25000, 'Cartão de crédito', 0, NULL, 7),
		 (8, 27000, 'Boleto', 1, '2025-06-10 10:30:00', 8),
		 (9, 30000, 'Pix', 0, NULL, 9),
		 (10, 22000, 'Dinheiro', 1, '2025-06-07 14:00:00', 10);
    -- Tabela Pagamentos  (FIM)
-- Inserindo dados nas tabelas (FIM)







