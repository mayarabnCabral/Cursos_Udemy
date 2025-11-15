"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
from datetime import datetime

horario = input('Que horas são? ')
horario_obj = datetime.strptime(horario, '%H:%M').time()


manha = horario_obj >= datetime.strptime('08:00', '%H:%M').time() and horario_obj <= datetime.strptime('11:59', '%H:%M').time()
madrugada = horario_obj >= datetime.strptime('00:00', '%H:%M').time() and horario_obj <= datetime.strptime('07:59', '%H:%M').time()
tarde = horario_obj >= datetime.strptime('12:00', '%H:%M').time() and horario_obj <= datetime.strptime('17:59', '%H:%M').time()
noite = horario_obj >= datetime.strptime('18:59', '%H:%M').time() and horario_obj <= datetime.strptime('23:59', '%H:%M').time()

horario_formatado = horario_obj.strftime("%H:%M")
try:
    if manha:
        if madrugada:
            print(f'Bom dia, mas vai dormir são {horario_formatado}')
        print(f'Bom dia! são {horario_formatado}')
    if tarde:
        print(f'Boa tarde! são {horario_formatado}')
    if noite:
        print(f'Boa noite! são {horario_formatado}')
except ValueError:
    print(f'Insira um horário valido, no formato H:M')