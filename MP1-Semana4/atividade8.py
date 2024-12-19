#Problema: Soletrando até acertar dessa vez

#Entrada
palavra_escolhida = str(input())
palavra_soletrada_certo = []
palavra_soletrada_crianca = []

#Aqui eu to soletrando corretamente a palavra escolhida
for i in palavra_escolhida:
  palavra_soletrada_certo.append(i)

#Aqui eu to coletando as letras que as criancas acham certas e verificando
while True:
  letra = str(input())
  if letra != ".":
    palavra_soletrada_crianca.append(letra)
  if letra == ".":
    if palavra_soletrada_crianca != palavra_soletrada_certo:
      palavra_soletrada_crianca = [] #isso serve para limpar a lista das letras erradas que a crianca pos antes
      print("8-|")
    if palavra_soletrada_crianca == palavra_soletrada_certo:
      print("8-)")
      break
  