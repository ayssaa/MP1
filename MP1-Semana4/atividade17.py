
#Problema: Imprimir a entrada até uma parada acontecer
#Entrada e Saida
string = ""

while True:
  string = str(input())
  if string == "CDA":
    print("CDA 1942")
    break
  if string != "":
    print(string)