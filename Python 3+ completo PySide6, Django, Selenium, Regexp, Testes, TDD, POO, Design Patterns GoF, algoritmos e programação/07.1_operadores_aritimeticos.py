"""
+ -> Adição 

- -> Subtração

* -> Multiplicação

/ -> Divisão
   -> O retorno sempre será um tipo float

// -> Divisão inteira
    -> O retorno é o quociente inteiro da divisão (arredonda para baixo)

** -> Exponenciação/poenciação

% -> Modulo 
    -> é o "resto" da divisão
     -> Muito utilizado para verificar se um número é múltiplo de outro, por exemplo
"""

adicao = 5 + 5
print('Adição: ', adicao)

subtracao = 5 - 5
print('Subtração:', subtracao)

multiplicacao = 5 * 5
print('Multiplicação: ', multiplicacao)

divisao = 10 / 3
print('Divisão: ', divisao)

divisao_inteira = 10 // 3.0
print('Divisão inteira: ', divisao_inteira)

exponenciacao = 10 * 2
print('Exponenciação: ', exponenciacao)

modulo = 55 % 2
print('Módulo: ', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)
