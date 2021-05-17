# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto  , custo):
    return (taxaImposto*custo) + custo
   
custo1 = float(input("digite o valor do produto:"))
taxa1 = 10/100
print(somaImposto(custo1,taxa1))

