nome = 'Mayara Bueno Nunes Cabral'
altura = 1.69
peso = 80
imc = peso / altura**2
classificacao= ...


linha_1 = f'{nome} tem {altura: .2f} de altura' # 0 .2f é referente as casas decimais que serão utilizadas 
linha_2 = f'pesa {peso} quilos e seu imc é : '
linha_3 = f'{imc: .10f}'

print(linha_1)
print(linha_2)
print(linha_3)

a = 'A'
b = 'B'
c = 1.1
string = 'a = {nome1} b = {nome2} c = {nome3:.2f}'
formato = string.format(
    
                            nome1 = a, nome2 = b, nome3 = c 
                        
                        
                        ) 
# Os valores serão preenchidos conforme os nomes indicados dentro das chaves {nome1}, {nome2}, etc.
# Também podemos usar preenchimento por ordem (sem nome): 'a = {} b = {} c = {:.2f}'
# Ou por índice: 'a = {0} b = {1} c = {2:.2f} a = {0}'

print(formato)