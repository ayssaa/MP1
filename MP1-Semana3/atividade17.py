#Problema: Dado votos, imprimir quantidade de votos em cada modalidade (v, f, outros)

#Entrada
numero_senadores = int(input())
favor = 0
contra = 0
outro = 0
for i in range(numero_senadores):
  voto = str(input())
  if voto == "F":
    favor += 1
  if voto == "C":
    contra += 1
  if voto == "A" or voto == "B" or voto == "N":
    outro += 1
    
#Saida
print("a favor:", favor)
print("contra:", contra)
print("outros:", outro)
