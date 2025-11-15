"""
Flags -> Marca um local ou condição
None -> Representa "nenhum valor" ou valor vazio
is -> Verifica se dois objetos são exatamente o mesmo (identidade)
is not -> Verifica se dois objetos não são o mesmo (não identidade)
"""

condicao = True
passou_no_if = None  # Inicialmente não passou no if

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# Verifica se a variável ainda está com valor None
if passou_no_if is None:
    print('Não passou no if')

# Verifica se a variável foi modificada (não é None)
if passou_no_if is not None:
    print('Passou no if')
