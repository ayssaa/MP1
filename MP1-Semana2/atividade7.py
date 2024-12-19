#Problema: dado uma idade, definir se a pessoa pode votar

#Entrada
idade = int(input())

#Saida
if idade >= 18 and idade < 70:
  print("Seu voto é obrigatório")
elif idade == 16 or idade == 17 or idade >= 70:
  print("Seu voto é facultativo: você pode votar ou não")
else:
  print("Jovem demais para votar, espere até 16")
  