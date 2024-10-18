
#Problema: Soletrando
#Entrada
palavra_escolhida = str(input())
palavra_soletrada_certo = []
palavra_soletrada_crianca = []

#Aqui eu to soletrando corretamente a palavra escolhida
for i in palavra_escolhida:
  palavra_soletrada_certo.append(i)

#Aqui eu to coletando as letras que as criancas acham certas
while True:
  letra = str(input())
  if letra != ".":
    palavra_soletrada_crianca.append(letra)
  if letra == ".":
    break

#Saida (e aqui eu comparo a palavra soletrada certo com a palavra soletrada da crianca)
if palavra_soletrada_certo == palavra_soletrada_crianca:
  print(True)
if palavra_soletrada_certo != palavra_soletrada_crianca:
  print(False)