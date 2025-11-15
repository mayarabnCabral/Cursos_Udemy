'''
Comentários em bloco: pode-se utilizar aspas simples (') ou duplas (") três vezes.

É necessário usar o mesmo caractere para abrir e fechar o bloco.
'''

# Comentário em linha: começa com o símbolo "#" e vai até o fim da linha

print('Olá mundo!') # Utilizado para exibir os dados na tela 

print(12, 34, sep='-') # O Sep é de separador e permite alterar o separador das informações do print
print(56, 78 , sep='separador')
print(90, 12 , sep='!')

print('Olá', end='...')  # end: Define o que será colocado no final da linha. Padrão é quebra de linha ('\n')
print('mundo!')

print('Olá', end='\n#')
print('mundo!')