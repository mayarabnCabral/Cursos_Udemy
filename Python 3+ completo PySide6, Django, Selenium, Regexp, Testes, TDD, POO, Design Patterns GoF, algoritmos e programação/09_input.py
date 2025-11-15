"""
input ->  Utilizado para coletar dados do usuário e armazenar em uma variável
       -> O valor retornado pelo input() é sempre do tipo string (str)
"""
nome = input('Qual é o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))

print(f'A soma dos numeros é: {numero_1 + numero_2}')