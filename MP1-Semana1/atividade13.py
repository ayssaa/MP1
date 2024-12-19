#Problema: O novo salario

# Entrada
salario = int(input ())
porcentagem = int(input ()) / 100 # dividido por 100 para virar porcentagem

# Calculando novo salário
salarioatual = (salario * porcentagem) + salario # parenteses pra especificar

# Saldo atual
print(salarioatual)
