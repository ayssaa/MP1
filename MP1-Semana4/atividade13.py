#Problema: Dado um número de vagas, imprimir quantas vagas sobram ou faltam

#Entrada
numero_vagas = int(input())
nome_aluna = ""
quantidade_aluna = 0

while True:
  nome_aluna = str(input())
  if nome_aluna != ".":
    quantidade_aluna += 1
  else:
    break

#Saida
if numero_vagas > quantidade_aluna:
  vagas_sobrando = numero_vagas - quantidade_aluna
  print("vagas sobrando:", vagas_sobrando)
if numero_vagas < quantidade_aluna:
  vagas_faltando = quantidade_aluna - numero_vagas
  print("vagas faltando:", vagas_faltando)
if numero_vagas == quantidade_aluna:
  print("vagas sobrando:", 0)
  