"""
Operaroers de atribuição -> Utilizados para Atribuir valores a variáveis 
                          -> = -> Atribuição simples (x = 10)
                          -> += -> Soma e atribui (x += 2  -> x = x + 2) 
                          -> -= -> Subtração e atribui (x -= 2  -> x = x - 2)
                          -> *= -> Multiplicação e atribui (x *= 2  -> x = x * 2)
                          -> **= -> Exponenciação e atribui (x **= 2 -> x = x ** 2)
                          -> /= -> Divisão e atribui (x /= 2  -> x = x / 2)
                          -> //= -> Divisão inteira e atribui (x //= 2 -> x = x // 2)
                          -> %= -> Módulo e atribui (x %= 2 -> x = x % 2)
"""



contador = 10
print(contador)

contador += 5   # contador = 15
print(contador)

contador -= 3   # contador = 12
print(contador)

contador *= 2   # contador = 24
print(contador)

contador **= 2  # contador = 576
print(contador)

contador /= 4   # contador = 144.0
print(contador)

contador //= 5  # contador = 28.0
print(contador)

contador %= 6   # contador = 4.0
print(contador)