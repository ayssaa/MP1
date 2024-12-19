#Problema: Dado um nome e uma variavel, remover os caracteres da variavel do nome

#Entrada
dados_aluna = str(input())
substituir = str(input())

for i in substituir:
  if i in dados_aluna:
    dados_aluna = dados_aluna.replace(str(i), "*")

#Saida
print(dados_aluna)
