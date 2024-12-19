#Problema: Dado quatro idades, achar a mais velha

#Entrada
idade1 = int(input())
idade2 = int(input())
idade3 = int(input())
idade4 = int(input())

#Saida
maior = idade1
if idade2 > maior:
  maior = idade2
if idade3 > maior:
  maior = idade3
if idade4 > maior:
  maior = idade4
print("A mais velha tem", maior, "anos")
