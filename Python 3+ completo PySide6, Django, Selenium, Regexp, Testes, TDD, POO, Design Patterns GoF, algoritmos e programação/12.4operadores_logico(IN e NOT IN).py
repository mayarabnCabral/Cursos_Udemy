"""
in -> Operador de verificação de existência
    -> Verifica se um valor está presente em uma sequência (como string, lista, tupla, etc)
    -> Retorna True se o valor for encontrado, senão retorna False

not in -> Operador de verificação negativa
        -> Verifica se um valor NÃO está presente em uma sequência
        -> Retorna True se o valor NÃO for encontrado, senão retorna False
"""

nome = 'Mayara'

print(nome[2]) # Utilizado para acessar um caracter de uma string

print(nome[-4])

print('y' in nome) # Estamos perguntando 'y' está na variável nome?
print('ma' in nome)
print(10 * '-')
print('y' not in nome) # Estamos perguntando 'y' não está na variável nome?
print('ma' not in nome)
print(10* '-')
validacao_nome = input('Digite deu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')