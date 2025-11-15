'''
Utilize a lista frutas do do desafio anterior, remova a manga da lista. depois remova o ultimo item da lista. Por fim imprima a lista modificada na tela 
'''

frutas = ['Maça', 'Banana', 'Manga', 'Uva', 'Abacaxi']

frutas.remove('Manga')
print(frutas)

del frutas[-1] 
print(frutas)