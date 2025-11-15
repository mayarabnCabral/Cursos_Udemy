"""
not -> Operador lógico "NÃO"
     -> Utilizado para inverter expressões
     -> Se o valor for verdadeiro, ele retorna falso
     -> Se o valor for falso, ele retorna verdadeiro
     -> Muito utilizado em condições para negar um valor ou resultado lógico
"""
senha = input('Senha: ')

if not senha:
    print('você não digitou nada')

# Avaliação de curto circuito
print(not 0)
print(not True)