# lendo uma string
string=input("Digite uma string: ")

# colocando toda string em minúscula
saida=string.lower()

# tirando todo espaço da string
x=saida.replace(" ","")


for i in x: # criando um laço para analisar cada caractere da string
    
    if i.isalpha(): # limitando apenas para caractere alfabético

        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u": # se conter as vogais, imprimir em caixa alta
            print(i.upper(),end="")
        else:
            print(i.lower(),end="") # caso contrário, imprimir em caixa baixa.


        
        
        




