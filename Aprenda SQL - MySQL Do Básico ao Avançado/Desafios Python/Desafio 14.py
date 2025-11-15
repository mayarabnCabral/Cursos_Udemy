'''
Crie um loop que imprima os numeros de 1 a 10, mas pare de imprimir assim que chegar a 5. Em seguida, crie um segundo loop que imprima os numeros de 1 a 10,, mas pule a impressão do numero 5.
'''
print('Loop com o break: ')
for n in range(1, 11):
    if n > 5:
        break
    print(n)

print('Loop com o continue: ')
for n in range(1, 11):
    if n == 5:
        continue
    print(n)