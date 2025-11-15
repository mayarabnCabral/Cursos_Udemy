"""
Interpolação -> Inserir valores de variáveis ou expressões dentro de uma string sem
                precisar concatenar manualmente
             -> s -> utilizado para string
             -> d e i -> utilizados para inteiros
             -> f -> utilizado para float
             -> x e X -> utilizados para hexadecimal (números formados por ABCDEF 0123456789)
                -> O x gera um hexadecimal minúsculo
                -> O X gera um hexadecimal maiúsculo
"""
variavel = 'ABCD'
print(f'{variavel}')        # sem formatação

print(f'{variavel: >10}')   # alinha à direita com espaços

print(f'{variavel:-<10}')   # alinha à esquerda com hífens

print(f'{variavel:-^10}')   # centraliza com '-'

print(f'{1000.54546445454551651678:,.1f}')  # separador de milhar, 1 casa decimal

print(f'{42:05d}')          # inteiro com 5 dígitos, zeros à esquerda

print(f'{1000.54546445454551651678:0>+10,.1f}')  # alinhado à direita, com zeros, sinal e separador