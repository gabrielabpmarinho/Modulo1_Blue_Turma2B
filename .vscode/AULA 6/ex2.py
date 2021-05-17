# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def funcao():
    perg = int(input("digite um numero:"))

    if perg == 0 :
        print("ZERO ,0 ")
    elif perg > 0:
        print("positivo, p")
    else :
        print("negativo , n")
funcao()