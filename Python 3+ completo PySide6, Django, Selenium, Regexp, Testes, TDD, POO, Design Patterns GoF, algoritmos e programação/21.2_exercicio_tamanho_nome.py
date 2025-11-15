"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto", se tiver 5 e 6, escreva (Seu nome é normal); maior que 6 escreva "Seu nome é muito grande"
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto')
if tamanho_nome == 5 and nome == 6:
    print('Seu nome é normal')
if tamanho_nome > 6:
    print('Seu nome é muito grande')