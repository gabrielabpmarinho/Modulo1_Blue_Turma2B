# 4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalha

def salario():
    horas = int(input("Digite a quantidade de horas trabalhadas:"))
    sal = 1100
    if horas >= 40:
       
        print("Salario de :",(horas - 40) * 1.5 + sal)
    else :
        print("Salario de :", sal / horas)


salario()