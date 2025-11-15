"""
while...else -> Estrutura específica do Python
              -> O bloco else só é executado se o while terminar "naturalmente"
              -> Se houver um break dentro do while, o else será ignorado
"""

string = 'Valor'

i = 0

while i < len(string):
    letra = string[i]
    print(letra)
    i += 1

    if letra == ' ':
        break  # se encontrar espaço, interrompe o laço
    
else:
    # só será executado se o laço acabar sem break
    print('Não foi encontrado espaço na string')

print('Fora do while')  # sempre executa
