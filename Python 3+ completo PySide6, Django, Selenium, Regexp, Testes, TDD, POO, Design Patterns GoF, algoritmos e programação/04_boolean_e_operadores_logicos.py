"""
bool -> Boolean
      -> Utilizado para "questionar" algo em um programa
       -> Só existe duas respostas possiveis Sim (True) ou Não (False)
        -> Existem vários operadores lógicos

Operadores lógicos -> Utilizados para "questionar" algo em um programa
                    -> == -> Operador que questiona se o valor é igual ao outro 
                    -> !=  -> diferente
                    -> <   -> menor que
                    -> >   -> maior que
                    -> <=  -> menor ou igual a
                    -> >=  -> maior ou igual a
                    -> and -> operador lógico "E" (ambas condições precisam ser verdadeiras)
                    -> or  -> operador lógico "OU" (pelo menos uma condição precisa ser verdadeira)
                    -> not -> operador lógico "NÃO" (nega a condição)
"""
# Igual a 
print(10==10)
print(10==15)
print(type(10==10))
print(type(10==15))

# Diferente
print(10 != 15)  
print(10 != 10)  

# Menor que
print(5 < 10)   
print(10 < 5)    

# Maior que
print(10 > 5)    
print(5 > 10)    

# Menor ou igual a
print(5 <= 5)   
print(4 <= 3)   

# Maior ou igual a
print(5 >= 5)    
print(3 >= 4)    

# and (E lógico)
print(True and True)   
print(True and False)   

# or (OU lógico)
print(True or False)    
print(False or False)  

# not (NÃO lógico)
print(not True)         
print(not False)       