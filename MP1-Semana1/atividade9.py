
#Problema: Receber dois valores inteiros, calcular.

# Entrada
valor1 = int(input ()) # valor1 int
valor2 = int(input ()) # valor2 int

# Calcular
soma = valor1 + valor2
subtração = valor1 - valor2
multiplicação = valor1 * valor2
divisão = valor1 / valor2
módulo = valor1 % valor2
divisãoint = valor1 // valor2
potência = valor1 ** valor2

# Imprimir resultado
print(soma)
print(subtração)
print(multiplicação)
print("%.2f" % divisão) # aqui é o único lugar que pode dar número decimal!
print(módulo)
print(divisãoint)
print(potência)