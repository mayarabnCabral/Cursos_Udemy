"""
for ... in -> Estrutura de repetição utilizada para iterar sobre sequências (como listas, strings, tuplas ou ranges)
            -> Loop definido, ou seja, sabe-se de antemão quantas vezes será executado
            -> Sintaxe básica:
                for item in sequencia:
                    # bloco de código
            -> Os comandos do while também podem ser utilizados no for (contiue, break e else, etc) 
"""


texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'|{letra}'
    print(letra)
print(novo_texto + '|')

