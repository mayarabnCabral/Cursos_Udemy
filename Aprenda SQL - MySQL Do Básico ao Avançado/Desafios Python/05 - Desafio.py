'''
Crie um script que soliciteao usuário dois numeros. Em seguida seu script deve imprimir a soma, a subtralçai, a multiplicação, a divisão(em decimal) e a exponenciação(primeiro numeo elevado ao segundo), desses dois numeros
'''

num1 = float (input('Digite um numero: '))
num2 = float (input('Digitie mais um numero: '))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
exp = num1 ** num2

print(f'Soma: {soma} ')
print(f'Subtração: {sub} ')
print(f'Multiplicação: {mult} ')
print(f'Divisão: {div} ')
print(f'Exponenciação: {exp} ')