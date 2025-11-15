"""
Fatiamento de strings -> Técnica para acessar partes específicas de uma string
                      -> Sintaxe: string[inicio:fim:passo]
                            -> inicio: índice inicial (inclusive), padrão 0
                            -> fim: índice final (exclusivo), padrão tamanho da string
                            -> passo: passo para avançar, padrão 1
                            -> Permite extrair substrings ou inverter strings

Função len -> utilizada para checar o tamanho de uma string 
           -> Sintaxe: len(nome_da_variavel)
"""
"""
 123456789
 Olá mundo
-987654321
"""

variavel = 'Olá mundo'
print(variavel[0:5])       # Imprime 'Olá m'

print(variavel[4:])        # Imprime do índice 4 até o final 'undo'

print(variavel[:5])        # Imprime do início até índice 4 'Olá m'

print(variavel[-8:-2])     # Índices negativos, imprime 'lá mun'

print(variavel[0:9:2])     # Passo 2, imprime caracteres de 2 em 2 'Oámn'

print(variavel[::-1])      # Inverte a string 'odnum aláO'

# Função len

print(len(variavel))       # Imprime o tamanho da string: 9
