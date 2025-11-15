"""
Formatação -> Permite controlar como valores são exibidos em uma string
            -> s -> utilizado para string
            -> d -> utilizado para inteiros
            -> f -> utilizado para float
            -> Inserção de caracteres para alinhamento:
                -> Sintaxe: {variavel:caractere_alinhamento>quantidade}
                -> > alinha à direita (preenchendo com o caractere à esquerda)
                -> < alinha à esquerda (preenchendo com o caractere à direita)
                -> ^ centraliza (preenchendo dos dois lados)
                -> = força o sinal (+ ou -) a aparecer antes dos zeros de preenchimento
            -> Separador de milhar:
                -> , (vírgula) insere separadores de milhar
            -> Casas decimais:
                -> .Nf onde N é o número de casas decimais
            -> Exemplos de especificadores:
                -> {variavel:10s}  -> string com largura 10
                -> {variavel:05d}  -> inteiro com 5 dígitos, preenchendo com zeros
                -> {variavel:,.2f} -> float com separador de milhar e 2 casas decimais
"""

variavel = 'ABCD'
print(f'{variavel}')        # sem formatação

print(f'{variavel: >10}')   # alinha à direita com espaços

print(f'{variavel:-<10}')   # alinha à esquerda com hífens

print(f'{variavel:-^10}')   # centraliza com '-'

print(f'{1000.54546445454551651678:,.1f}')  # separador de milhar, 1 casa decimal

print(f'{42:05d}')          # inteiro com 5 dígitos, zeros à esquerda

print(f'{1000.54546445454551651678:0>+10,.1f}')  # alinhado à direita, com zeros, sinal e separador

print(f'{1000.54546445454551651678:0=+10,.1f}')  # Número com sinal (+), preenchido com zeros à esquerda, sinal antes dos zeros, largura total 10, separador de milhar e 1 casa decimal

