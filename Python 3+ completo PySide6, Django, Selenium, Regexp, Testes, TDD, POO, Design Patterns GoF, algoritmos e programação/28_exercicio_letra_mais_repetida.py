"""
Verifique qual letra mais teve repetição com while
"""

frase = 'O Python é uma linguagem de programação.' \
        'multiparadigima.' \
        'Python foi criado por Guido Van Rossum.'
print(frase)


i = 0 
qtd_mais_apareceu = 0
while i < len(frase):
    letra_atual = frase[i]
    # print(letra_atual)
    

    if letra_atual.strip(): # Ignota os espaços
        qtd_atual = frase.count(letra_atual) # Conta quantas vezes aparece a letra atual do while

        # Verifica se a quantidade atual é a maior registrada se sim atualiza  aletra e quantidade 
        if qtd_mais_apareceu < qtd_atual:       
            qtd_mais_apareceu = qtd_atual       
            letra_mais_apareceu = letra_atual   

    i += 1

print(f'A letra que mais apareceu foi "{letra_mais_apareceu.upper()}" com {qtd_mais_apareceu} repetições')    