#Problema: Joaninha de brinquedo!
#Entrada
bateria = int(input())
avancar = 1
virar = 5

#Processo
while bateria > 5:
  bateu_livre = str(input())
  abismo_piso = str(input())
  if bateu_livre == "B" or abismo_piso == "A":
    bateria = bateria - virar
    print("virar:", bateria)
  else:
    bateria = bateria - avancar
    print("avançar:", bateria)

#Saida
print("recarregar:", bateria)