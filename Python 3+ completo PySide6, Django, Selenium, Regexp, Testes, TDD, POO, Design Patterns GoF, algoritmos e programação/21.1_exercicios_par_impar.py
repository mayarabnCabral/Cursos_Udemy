"""
Faça um programa que peça ao usuário para digitar um número inteiro, informar se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""

numero = input('Digite um numero inteiro: ')

try:
    numero = float(numero)
    par_ou_impar = numero % 2
    if par_ou_impar == 0:
        print('Seu numero é par')
    else:
        print('Seu numero é impar')
except ValueError:
    print('O numero digitado não e inteiro')