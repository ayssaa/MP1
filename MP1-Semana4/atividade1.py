#Problema: Transformando entradas de base 2 em saidas de base 10

#Entrada
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())

#Transformando
valor_base10 = valor1*(2**3)+valor2*(2**2)+valor3*(2**1)+valor4*(2**0)

#Saida
print(valor_base10)
