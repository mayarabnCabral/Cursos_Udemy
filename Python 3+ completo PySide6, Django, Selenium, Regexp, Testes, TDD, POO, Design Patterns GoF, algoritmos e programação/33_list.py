"""
list -> Listas
     -> Mutável
     -> Suporta vários valores de qualquer tipo
     -> list()
     -> []
"""
# ........0....1.......2.......3....4
lista = [123, True, 'Mayara', 1.5, []]
#........-5....-4......-3.....-2...-1

# print(bool(lista)) # Lista vazia é igual a False
# print(lista, type(lista))
print(lista[2], type(lista[2])) # Acessando o índice 2 da lista

lista[2] = 'Mariana' # Alterando o valor do índice 2 da lista
print(lista[2], type(lista[2]))