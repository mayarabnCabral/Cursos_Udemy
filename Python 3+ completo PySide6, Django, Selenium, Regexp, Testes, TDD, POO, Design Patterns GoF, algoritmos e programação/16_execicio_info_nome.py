"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    exiba:
    seu nome é {nome}
    seu nome invertido é {nome invertido}
    seu nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu noma é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios"
"""
nome = input('Digite um nome: ')
idade = input('Digite uma idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido {nome[::-1]}')

    if nome == " ":
        print(f'Seu nome tem espaços')
    else:
        print(f'Seu nome não espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu noma é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')