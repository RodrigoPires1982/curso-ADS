def referenciaAutor(str):

    y=str.split()  # transformando cada palavra em um item

    z=str.replace(y[len(y)-1],"") # Retirando o ultimo sobrenome da string

    print("{}, {}".format(y[(len(y)-1)].upper(),z)) # impressão formatada com o ultimo elemento da lista y e a string sem o último sobrenome



# chamada da função
referenciaAutor(input("Digite o nome do autor: "))

