#Problema: Email...

#Entrada
c = int(input())
contador = 0

#Saida
for num in range(c):
  email = input()
  if "@" not in email:
    contador = contador + 1
print(contador)