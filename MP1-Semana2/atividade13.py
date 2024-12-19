#Problema: Dado dois valores e uma operação, achar resultado

#Entrada
opr = str(input())
valor1 = int(input())
valor2 = int(input())

#Saida
if "+" == opr:
  resul = valor1 + valor2
  print(resul)
elif "-" == opr:
  resul = valor1 - valor2
  print(resul)
elif "*" == opr:
  resul = valor1 * valor2
  print(resul)
elif "/" == opr:
  resul = valor1 / valor2
  print(resul)
elif "//" == opr:
  resul = valor1 // valor2
  print(resul)
elif "%" == opr:
  resul = valor1 % valor2
  print(resul)
elif "**" == opr:
  resul = valor1 ** valor2
  print(resul)
  