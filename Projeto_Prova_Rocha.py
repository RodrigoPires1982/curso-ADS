
from random import randint
# lendo a ordem da Matriz e o fator escalar
n=int(input("n: "))
x=int(input("x: "))
print()

# função para imprimir a matriz
def matriz(M):
    for i in range(n):
        for j in range(n):
            print(M[i][j],end=" ")

        print()




# criando a Matriz A utilizando a random
print("Matriz A:")
Matriz_A=[]
for i in range(n):
    linha = []
    for j in range(n): 
        linha.append( randint(1,10))

    Matriz_A.append(linha)

matriz(Matriz_A) # chamada da função


print()
print("Matriz B:")  

# criando a Matriz B com a função random 
Matriz_B=[]
for i in range(n):
    linha1 = []
    for j in range(n): 
        linha1.append( randint(1,10))

    Matriz_B.append(linha1)

matriz(Matriz_B)



print()
print("Matriz AT:")

# criando a Matriz transposta de A
Matriz_AT=[]
for i in range(n):
    linha2 = []
    for j in range(n): 
        linha2.append(Matriz_A[j][i])  # inverte o índice da linha pela coluna

    Matriz_AT.append(linha2)

matriz(Matriz_AT)   # chamada da função


print()
print("Matriz x*AT:")



# multiplicando o fator escalar pela Matriz transposta da Matriz A
Matriz_xAT=[]
for i in range(n):
    linha3 = []
    for j in range(n): 
        linha3.append((Matriz_A[j][i])*x) # multiplicando cada elemento pelo fator escalar

    Matriz_xAT.append(linha3)


matriz(Matriz_xAT)  # chamada da função



print()
print("Matriz B <TS>:")

# criando a Matriz triangular a partir da Matriz B
Matriz_BTS=[]
for i in range(n):
    linha4 = []
    for j in range(n):
        if i > j:          # condicional, caso a linha seja maior que a coluna
         linha4.append(0)   
        else:
         linha4.append((Matriz_B[i][j]))

    Matriz_BTS.append(linha4)

matriz(Matriz_BTS)  # chamada da função


print()
print("Matriz C:")

# criando a Matriz C somando os elementos equivalentes da Matriz X*AT com os elementos da Matriz B <TS>
Matriz_C=[]
for i in range(n):
    linha5 = []
    for j in range(n):
        linha5.append((Matriz_BTS[i][j]+Matriz_xAT[i][j]))

    Matriz_C.append(linha5)

matriz(Matriz_C) # chamada da função
