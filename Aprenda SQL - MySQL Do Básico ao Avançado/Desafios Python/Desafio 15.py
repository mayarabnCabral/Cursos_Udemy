'''
Crie uma lista de frutas que inclui maça três vezes e outras frutas de sua escola. Use loop for para contar quantas vezes maça aparece na lis e imprima o resultado
'''
frutas = ['Maçã','Melancia','Maçã', 'Melancia', 'Melancia', 'Melancia', 'Banana','Manga', 'Maçã', 'Banana', 'Melancia']
contador_maca = 0

for maca in frutas:
    if maca == 'Maçã':
        contador_maca += 1
print(f'Temos {contador_maca} Maçã(s)')

'''
extras
'''
contador_melan = 0
contador_banana = 0
contador_manga = 0

for melan in frutas:
    if melan == 'Melancia':
        contador_melan += 1
print(f'Temos {contador_melan} Melancia(s)')

for banana in frutas:
    if banana == 'Banana':
        contador_banana += 1
print(f'Temos {contador_banana} Banana(s)')

for manga in frutas:
    if manga == 'Manga':
        contador_manga += 1
print(f'Temos {contador_manga} Manga(s)')