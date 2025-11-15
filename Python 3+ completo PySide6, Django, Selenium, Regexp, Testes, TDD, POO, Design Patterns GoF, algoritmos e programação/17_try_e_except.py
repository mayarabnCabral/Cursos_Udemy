"""
try -> Tenta executar um bloco de código que pode gerar erro
except -> Captura o erro que ocorreu no try e permite tratar ou mostrar uma mensagem personalizada

OBS.: Não é correto utilizar o try except como o exemplo, só foi utilizado para mostrar o conceito 
"""

numero_str = input('Vou dobrar o numero que você digitar: ')

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float  * 2:.2f}')
except:
    print('Isso não é um numero')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(numero_str.isdigit()) # isdigit verifica se o usuário digitou apenas numeros
#     print(f'O dobro de {numero_str} é {numero_float  * 2:.2f}')
# else:
#     print('Isso não é um numero')