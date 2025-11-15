nome = 'Mayara'
sobrenome = 'Bueno Nunes Cabral'
idade = 23
ano_nascimento = 2025 - idade
maior_de_idade = idade >= 18
altura_metros = 1.65

# melhorando um pouco 
if maior_de_idade: 
        maior_de_idade = f'\033[32mSim\033[0m'
else:
        maior_de_idade = '\033[31mNão\033[0m'

print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de nascimento: ', ano_nascimento)
print(f'É maior de idade? {maior_de_idade}')
print('Altura em metros: ', altura_metros)


