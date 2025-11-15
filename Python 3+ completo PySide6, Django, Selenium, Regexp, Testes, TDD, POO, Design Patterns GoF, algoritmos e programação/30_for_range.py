"""
range -> Retorna uma sequência numérica, que pode ser convertida em uma lista.
         -> Pode receber um, dois ou três parâmetros (start, stop, step)
"""

# numero = range(10)  # 0 a 9
# print(list(numero))

# numero = range(5, 10)  # 5 a 9
# print(list(numero))

# numero = range(0, 10, 2)  # 0 a 9 de 2 em 2
# print(list(numero))

numero = range(10)

for numeros in numero:
    print(numeros)
print('-' * 10)

# _____________________________________________

numero = range(5,10)

for numeros in numero:
    print(numeros)
print('-' * 10)

# _____________________________________________

numero = range(0,10,2)

for numeros in numero:
    print(numeros)
print('-' * 10)