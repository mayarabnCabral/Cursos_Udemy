"""
Faça uma calculadora com while
"""



while True:
    
    n1 = input('Informe o primeiro numero: ')
    operador = input('Informe o operador: ')
    n2 = input('Informe o segundo numero: ')

    n_validos = None

# Tratamento para caso o usuário não informe numeros 
    try:
        n1_tratado = float(n1)
        n2_tratado = float(n2)
    except:
        n_validos = None 
        if n_validos is None:
            print('Um ou ambos os numeros digitados não são validos')
            continue

    operadores_permitidos = '+-*/'

    if len(operador) != 1:
        print('Digite apenas um operador')
        continue
    
    if operador not in operadores_permitidos:
        print('O operador digitado não é permitido')
        continue

    if operador == '/' and n2_tratado == 0.0:
        print('Divisão por zero não é permitido')
        continue

    
    if operador == '+':
        total = n1_tratado + n2_tratado
        print(f'{n1_tratado} {operador} {n2_tratado} = {total}')

    elif operador == '-':
        total = n1_tratado - n2_tratado
        print(f'{n1_tratado} {operador} {n2_tratado} = {total}')

    elif operador == '*':
        total = n1_tratado * n2_tratado
        print(f'{n1_tratado} {operador} {n2_tratado} = {total}')

    elif operador == '/':
        total = n1_tratado / n2_tratado
        print(f'{n1_tratado} {operador} {n2_tratado} = {total}')
    
    sair = input('Deseja sair? [s]im ').lower().startswith('s')

    if sair == True:
        break

    