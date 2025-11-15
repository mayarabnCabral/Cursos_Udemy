"""
and -> É um operador lógico
     -> Todas as condições precisam ser verdadeiras
     -> Se qualquer valor for considerado falso, a expressão inteira será avaliada como esse valor
        -> Exemplos de valores considerados falsos: 0, 0.0, '', False, None (usado para representar um não valor)
    -> Ele para no primeiro valor falso que encontrar
     -> Se todos os valores forem verdadeiros, retorna o último valor avaliado
""" 
entrada = input('Digite "E" para entrar ou "S" para sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar') 
elif entrada == 'S'and senha_digitada == senha_permitida:
    print('Sair')
else:
    print('Hum... tem algo errado, tente novamente')

    # Avaliação de curto curcuito

    print(True and 0 and False)