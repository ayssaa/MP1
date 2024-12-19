#Problema: Um placar de volei digital!

#Variaveis do placar
placar_time1 = 0
placar_time2 = 0

#Contagem de pontos que finaliza quando alguem ganha ou ambos chegam no set-point
while True:
  pontos = int(input())
  if pontos == 1:
    placar_time1 += 1
  if pontos == 2:
    placar_time2 += 1
  if placar_time1 == 25 or placar_time2 == 25 or placar_time1 == 24 and placar_time2 == 24:
    break

#Se estiverem em set-point, esse if roda e finaliza somente com uma diferença de 2 pontos
if placar_time1 == 24 and placar_time2 == 24:
  while True:
    pontos = int(input())
    if pontos == 1:
      placar_time1 += 1
    if pontos == 2:
      placar_time2 += 1
    if (placar_time1 - placar_time2) == 2:
      break
    if (placar_time2 - placar_time1) == 2:
      break

#Saida
print(placar_time1, "x", placar_time2)
