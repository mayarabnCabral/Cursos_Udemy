"""
id -> Identificador
    -> A função mostra o endereço do valor na memória
    -> Caso os valores sejam iguais, pode ser que o id também seja igual
       (em Python isso ocorre devido ao mecanismo de interning de strings)
"""

v1 = 'a'
v2 = 'a'
v3 = 'b'

print(id(v1))  # Mostra o id/identificador de v1
print(id(v2))  # Mostra o id/identificador de v2 (geralmente igual ao de v1)
print(id(v3))  # Mostra o id/identificador de v3 (diferente)
