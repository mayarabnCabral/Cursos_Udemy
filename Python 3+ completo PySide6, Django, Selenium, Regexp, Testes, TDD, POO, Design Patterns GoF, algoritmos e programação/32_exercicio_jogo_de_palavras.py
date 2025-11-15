"""
Faça um jogo para o usuário adivinhar a palavra secreta.
Você vai propor uma palavra secreta qualquer e o usuário vai digitar apenas uma letra.
Quando o usuário digitar uma letra confira se a letra digitada está na palavra secreta.
         Se a letra digitada estiver na palavra secreta, exiba a letra.
            Se a letra digitada não estiver na palavra secreta, exiba *.
Faça a contagem de tentativas do usuário.
"""

import random

palavras_possiveis = ['banana', 'abacaxi', 'laranja', 'manga', 'melancia', 'uva', 'pera',
                       'jabuticaba', 'caju', 'goiaba', 'perfume', 'computador', 'celular',
                       'teclado', 'mouse', 'monitor', 'amor', 'vida', 'morte', 'carro', 'moto',
                       'barco', 'navio', 'trem', 'bicicleta', 'futebol', 'basquete', 'volei',
                       'tenis', 'xadrez', 'dama', 'buraco', 'truco', 'desenvolvimento', 
                       'tecnologia', 'internet', 'rede', 'sistema', 'software', 'hardware',
                       'aplicativo', 'jogo', 'jogador', 'time','torcida', 'gol', 'ponto', 
                       'falta', 'pagamento', 'vindadores', 'mulher', 'homem', 'adulto', 'idoso', 
                       'amigo', 'inimigo', 'paz', 'guerra', 'felicidade', 'tristeza', 'alegria', 
                       'raiva', 'medo', 'coragem', 'fraqueza', 'cachorro', 'gato', 'coelho', 
                       'girafa', 'leopardo', 'macaco', 'zebra']

while True:
    palavra_secreta = random.choice(palavras_possiveis).upper()
    letra_acerto = ''
    tentativas = 0
    palavra_formada = '*' * len(palavra_secreta)
    

    print('A palavra secreta é: ', palavra_formada)
    
    while palavra_formada != palavra_secreta:
        letra_digitada = input('Digite uma letra: ').upper()
        tentativas += 1
        
        if len(letra_digitada) != 1:
            print('Digite apenas uma letra.')
            continue
        
        if letra_digitada in palavra_secreta:
            letra_acerto += letra_digitada
        
        palavra_formada = ''
        for letra in palavra_secreta:
            if letra in letra_acerto:
                palavra_formada += letra
            else:
                palavra_formada += '*'
        
        print(palavra_formada)
    
    print(f'\nParabéns! Você ganhou! A palavra era {palavra_formada}.')
    print(f'Você precisou de {tentativas} tentativas para acertar {len(palavra_secreta)} letras.')
    print(f'Sua porcentagem de acerto foi de {len(palavra_secreta) / tentativas * 100:.2f}%.')

    sair = input('Digite "sair" para encerrar ou pressione Enter para continuar: ').upper()
    if sair == 'SAIR':
        print('Obrigada por jogar!')
        break
