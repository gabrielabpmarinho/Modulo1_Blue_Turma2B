# 6.	Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).


# Nota	Conceito
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# <=4.0	F




def conceito():
    
    if nota >= 9 :
        print('conceito A')
    elif > = 8 :
        print('conceito B')
    elif > = 7 :
        print("conceito C")
    elif > = 6 :
        print("conceito D")
    elif < 6 and > 4 :
        print("conceito E")
    else :
        print("conceito F")

nota = float(input("digite sua nota:"))
conceito(nota)

