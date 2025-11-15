"""
continue -> Utilizado para "pular" uma iteração dentro do loop
          -> Quando o Python encontra o continue, ele interrompe a execução 
             daquela repetição e vai direto para a próxima
"""

contador = 0 

while contador <= 100:
    contador += 1

    if contador == 2:
        print("Não vou mostar o 2")
        continue
    

    if contador >= 10 and contador <= 27:
        #print(f'Não vou mostar o {contador}')
        continue

    if contador == 40:
        break
    
    print(contador)

print('Acabou')