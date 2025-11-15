"""
Utilizando While verifique o nome do usuário, e inprima o nome separando as letras com "|"
"""
#.......123456
nome = 'Mayara'
# - ....654321

tamanho_nome = len(nome)
print(f'Seu nome é: {nome}')
print(f'Seu nome tem {tamanho_nome} letras')

nova_str = '' # Str vazia para acumular as letras com o *
letra = 0
while letra < tamanho_nome:
    nova_str += nome[letra] + '|' # '+=' acumula cada letra + '*', sem apagar o que já estava
    letra += 1
print(nova_str)