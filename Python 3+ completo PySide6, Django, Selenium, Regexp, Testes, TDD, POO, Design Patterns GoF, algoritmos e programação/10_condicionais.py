"""
if -> Se
    -> Utilizado para dar uma condição para rotar certa parte do codigo
     -> if condição: print()
      -> pode ser utilizado sozinho 

elif -> Senão, se
      -> Usado para testar uma nova condição, caso a anterior (if ou outro elif) seja falsa
       -> Não pode ser utilizado sem um if 

else -> Se não
      -> Executa um bloco de código se todas as condições anteriores forem falsas.
       ->  Não pode ser utilizado sem um if 
"""
entrada = input('Você quer "entrar" ou "sair" ')

# if
if entrada == 'entrar':
    print('Você emtrou no sistema, seja bem vindo :D')
elif entrada == 'sair':
    print('Você saiu do sistema, até logo :)')
elif entrada == 'não sei':
    print('Sai de cima do muro, se decida >( por favor ')
else:
    print('Você não digitou nenhuma das opções :(')