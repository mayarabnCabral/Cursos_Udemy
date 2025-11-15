'''
Crie uma lista de frutas e outra de vergetais. Use um for loop anunhado (nested for loop) para imprimir todas as combinações possiveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo
'''

frutas = ['Melancia', 'Maça', 'Manga']
vegetais = ['Cenoura', 'Brocolis', 'Couve']

for fruta in frutas:
    for vegetal in vegetais:
        print(f'{fruta} e {vegetal}')