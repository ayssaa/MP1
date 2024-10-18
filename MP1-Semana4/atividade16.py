
#Problema: Dado strings, imprimir quantas foram entradas
#Entrada
quantidade_string = 0
string = ""

while True:
  string = str(input())
  if string == "CDA 1942":
    break
  if string != "":
    quantidade_string += 1

#Saida
print(quantidade_string)