"""
Laços internos -> Também chamados de "loops aninhados"
                -> É quando um laço de repetição está dentro de outro
                -> O loop interno executa completamente a cada repetição do loop externo
                -> Muito usado para trabalhar com tabelas, matrizes e combinações
                -> Cuidado: loops aninhados aumentam a complexidade do código
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1  # contador para o loop externo (linhas)

while linha <= qtd_linhas:  # loop externo controla as linhas
    coluna = 1  # contador para o loop interno (colunas)
    while coluna <= qtd_colunas:  # loop interno controla as colunas
        print(f'{linha=} {coluna=}')  # mostra os índices atuais
        coluna += 1  # incrementa a coluna
    linha += 1  # quando o loop interno termina, passa para a próxima linha

print('Acabou')  # executa no fim de tudo
