#Problema: Dado valores em base 10, imprimir o dobro do que ele representa
#Entrada
milhar = int(input())
centena = int(input())
dezena = int(input())
unidade = int(input())

#Calculando
dobro = 2 * (milhar*(10**3) + centena*(10**2) + dezena*(10**1) + unidade*(10**0))

#Saida
print(dobro)