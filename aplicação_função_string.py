print("Este ano, o ganhador do Prêmio Nobel será o escritor que mais vendeu livros.  ")
print("Para isso é necessário que lance o número de livros vendidos por cada escritor. ")
print()

#Recebendo a quantidade de livros vendidos
A=int(input("Quantos livros vendeu o escritor Machado de Assis: "))
B=int(input("Quantos livros vendeu o escritor Jorge Luís Borges: "))
C=int(input("Quantos livros vendeu o escritor Clarice Lispector: "))
D=int(input("Quantos livros vendeu o escritor Luís de Camões: "))
print()
#lista com os livros vendidos
lista=[A,B,C,D]

#Função para encontrar o maior numero da lista
Resultado_final=max(lista, key=int)


def referenciaAutor(str):

    y=str.split()  # transformando cada palavra em um item

    z=str.replace(y[len(y)-1],"") # Retirando o ultimo sobrenome da string

    print("Com {} livros vendidos, o escritor vencedor foi: {}, {}".format(Resultado_final,y[(len(y)-1)].upper(),z)) # impressão formatada com o ultimo elemento da lista y e a string sem o último sobrenome



# chamada da função de forma condicionada
if lista[0] == Resultado_final:
    referenciaAutor(("Machado de Assis"))
elif lista[1] == Resultado_final:
    referenciaAutor(("Jorge Luís Borges"))
elif lista[2] == Resultado_final:
    referenciaAutor(("Clarice Lispector"))
elif lista[3] == Resultado_final:
    referenciaAutor(("Luís de Camões"))