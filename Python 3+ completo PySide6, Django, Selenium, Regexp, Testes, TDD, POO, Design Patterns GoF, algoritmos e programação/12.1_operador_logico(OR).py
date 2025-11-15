"""
or -> Operador lógico "OU"
    -> Apenas uma condição precisa ser verdadeira para o resultado ser verdadeiro
    -> Ele para no primeiro valor verdadeiro que encontrar
    -> Se todos os valores forem falsos, retorna o último valor avaliado
    -> Exemplos de valores considerados falsos: 0, 0.0, '', False, None (usado para representar um não valor)
"""

entrada = input('Digite "E" para entrar ou "S" para sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar') 
elif (entrada == 'S'or entrada == 's') and senha_digitada == senha_permitida:
    print('Sair')
else:
    print('Hum... tem algo errado, tente novamente')

# Avaliação de curto circuito
 
print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)