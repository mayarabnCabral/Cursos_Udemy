"""
append() -> Adiciona um item ao final da lista
     
insert() -> Adiciona um item no índice escolhido
    
pop() -> Remove o último item da lista ou o índice escolhido

del -> Remove um item pelo índice ou fatiamento
     
clear() -> Remove todos os itens da lista
      
extend() -> Adiciona mais de um item ao final da lista

+ -> Concatena listas
    
"""

lista = [10, 20, 30, 40, 50]
lista[2] = 300 # Alterando o valor do índice 2 da lista
print(f'Após alterar o indice 2: {lista}, alterado para: {lista[2]}')

del lista[-1] # Removendo o valor o ultimo índice da lista
print(f'Após utilizar o del: {lista}')

lista.append(60) # Adicionando o valor 50 ao final da lista
print(f'Após append: {lista}')

lista.insert(0, 5) # Adicionando o valor 5 no índice 0 da lista
print(f'Após utilizar insert 2: {lista}')

lista.pop() # Removendo o último valor da lista
ultimo_valor = lista.pop(2) # Removendo o valor do índice 2 da lista
print(f'Após utilizar pop:  {lista}, Removido: {ultimo_valor}')

lista.clear() # Limpando a lista
print(f'Após utilizar clear: {lista}')

lista_a = [1, 2, 3]
lista_b = [4, 5, 6] 

lista_c = lista_a + lista_b # Concatenando as listas
print(f'Após concatenar as listas: {lista_c}')

lista_a.extend(lista_b) # Adicionando os valores da lista_b ao final da lista_a
print(f'Após utilizar extend: {lista_a}')


