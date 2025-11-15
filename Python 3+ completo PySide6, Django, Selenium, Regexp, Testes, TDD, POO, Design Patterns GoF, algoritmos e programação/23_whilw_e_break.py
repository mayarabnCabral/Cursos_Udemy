"""
while -> Enqunato
       -> Laço de repetição
        -> executa uma ação enquanto uma condição for verdadeira
        -> Utilizado quando não sabemos quantas vezes o loop deve ser executado
       -> Sintaxe básica:   
            while condição:
                # bloco de código

break -> quebra(parar)
       -> Utilizado para parar o laço de repetição
Loop infinito -> Quando um código não tem fim
"""
condicao = True

# while condicao:  #Loop infinito sem o break
#     print('1')
#     print('2')
#     print('3')

# while condicao:
#     nome = input('Qual é o seu nome: ')
#     print(f'Seu nomeé {nome}')
#     break

quantas_vezes = int(input('Quantas vezes deseja repetir: '))
contador = 0

while contador < quantas_vezes:
    contador += 1
    print(f"{contador}")
print('Acabou!')