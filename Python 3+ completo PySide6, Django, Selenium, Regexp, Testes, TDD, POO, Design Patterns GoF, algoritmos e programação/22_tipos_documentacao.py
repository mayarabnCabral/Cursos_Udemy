"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Alguns tipos de dados imutáveis: str, int, float, bool
"""

string = 'mayara'
outra_variavel = string  # Estou criando uma nova variável que referencia o mesmo valor (objeto imutável) da variável string

# string[3] = "ABC"  # Não tem como alterar o valor da string, por ser imutável
# print(string[3])   # Isso causaria um erro se descomentado


mais_variavel = f'{string[:3]}ABC{string[4:]}'# Para "alterar" parte de uma string, criamos uma nova string com a modificação desejada
print(mais_variavel) # Saída esperada: mayABCra (substituindo o caractere no índice 3)


print(string.capitalize()) # capitalize(): Deixa apenas a primeira letra da string em maiúscula


print(string.zfill(100)) # zfill(n): Preenche a string à esquerda com zeros até que ela tenha n caracteres