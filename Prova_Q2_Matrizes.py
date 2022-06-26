
Matriz = [] #criando uma matriz


#recebendo linha e colunas
Q_linha = int(input("Digite o número de linhas: "))
Q_coluna = int(input("Digite o número de colunas: "))


# inserindo os elementos na matriz 
for i in range(Q_linha):
    linha = []
    for j in range(Q_coluna): 
        linha.append( input("A%i%i: " % (i, j) ) )

    Matriz.append(linha)
    
print("Matriz Aleatória")

# imprimindo a matriz
for i in range(Q_linha):
  for j in range(Q_coluna):
    print(Matriz[i][j],end=" ")
  print()
print()
print("Matriz Ordenada")



# criando a lista novamente para oredenar os elementos
y=[]
for i in range(Q_linha):
    
    for j in range(Q_coluna):
        y.append(Matriz[i][j])

# usando a função sorted dentro de outra função para ordenar os elementos
def ordenamatriz(N):
    s=sorted(N)
    return s
    
#criando a matriz novamente , mas com os elementos ordenados
def montandomatriz(lista,n):
    for i in range(0,len(lista),n):
        yield lista[i:i+n]

#chamada da função ordenar
recebe=ordenamatriz(y)


#chamada da função que monta a matriz ordenada
matriz2= list(montandomatriz(recebe,Q_coluna))

#imprimndo a matriz ordenada
for i in range(Q_linha):
    for j in range(Q_coluna):
        print(matriz2[i][j],end=" ")
    print()
print()









   
        
    




