"""
Python -> linguagem de programação
        -> É uma limguagem de tipagem dinâmica e forte

string / str -> São dados do tipo texto
              -> Devem ser informadas entre aspas simples (' ') ou duplas (" ")
"""

# Aspas simples
print('Mayara Bueno Nunes Cabral')
print('Mayara "Bueno" Nunes Cabral\n')

# Aspas duplas
print("Mayara Bueno Nunes Cabral")
print("Mayara 'Bueno' Nunes Cabral\n")

# Escape: usado para inserir caracteres especiais dentro de strings

print("Mayara \"Bueno Nunes Cabral")  # \" permite colocar aspas duplas dentro de uma string com aspas duplas
print("Mayara \'Bueno Nunes Cabral\n")  # \' permite colocar aspas simples dentro de uma string com aspas duplas

# r: prefixo que transforma a string em "raw string" (string bruta)
# Isso faz com que os caracteres de escape (como \n, \t, \") sejam interpretados literalmente
print(r"Mayara \'Bueno Nunes Cabral")