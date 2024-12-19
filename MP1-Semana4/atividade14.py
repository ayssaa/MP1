#Problema: Imprimir quantos accepts uma aluna conseguiu

#Entrada
accept = 0
resposta = ""

while resposta != "timeout":
  resposta = str(input())
  if resposta == "accepted":
    accept += 1

#Saida
print(accept)
