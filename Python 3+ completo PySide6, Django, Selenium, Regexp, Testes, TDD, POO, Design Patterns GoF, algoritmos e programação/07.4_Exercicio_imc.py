nome = 'Mayara Bueno Nunes Cabral'
altura = 1.69
peso = 80
imc = peso / altura**2
classificacao= ...

if imc <= 16:
    classificacao = '\033[31mMagreza grave\033[0m'
elif 16 < imc <= 16.9:
    classificacao = '\033[31mMagreza moderada\033[0m'
elif 16.9 < imc <= 18.4:
    classificacao = '\033[33mMagreza leve\033[0m'
elif 18.4 < imc <= 24.9:
    classificacao = '\033[32mPeso normal (adequado)\033[0m'
elif 24.9 < imc <= 29.9:
    classificacao = '\033[33mSobrepeso\033[0m'
elif 29.9 < imc <= 34.9:
    classificacao = '\033[31mObesidade grau I\033[0m'
elif 34.9 < imc <= 39.9:
    classificacao = '\033[31mObesidade grau II (severa)\033[0m'
else:
    classificacao = '\033[41mObesidade grau III (mórbida)\033[0m'



print(f'{nome} tem {altura} de altura pesa {90} e seu IMC é {imc:.2f} e está classificada(o) como {classificacao}')