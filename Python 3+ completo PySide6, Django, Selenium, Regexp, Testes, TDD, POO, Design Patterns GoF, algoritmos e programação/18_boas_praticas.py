"""
CONSTANTE -> "Variavies" que não vão mudar 

Utilizar muitos ifs não é legal
"""

velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local atual do carro 

# Quando temos uma constante é legal digitarmos em letra maiuscula
RADAR_1 = 60
LOCAL_1 = 100 # 100 m
RADAR_RANGE = 1 # Distancia onde o radar pega

# Resumido o codigo
velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade_carro_passou_radar_1
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if carro_passou_radar_1:
    print(f'A velocidade do carro está acima da permitida')

if carro_multado_radar_1:

    print(f'carro multado em radar 1')
