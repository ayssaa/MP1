#Problema: Dado três valores, achar o número de raízes da equação

#Entrada
A = float(input())
B = float(input())
C = float(input())

#Continha
x = B**2 - 4*A*C

#Saida
if x < 0:
  print(0)
if x == 0:
  print(1)
if x > 0:
  print(2)