#Problema: dado uma senha, verificar parametros definidos

#Entrada
senha = str(input())
caracteres = 0
vogais = 0
digitos = 0
for i in senha:
  caracteres += 1
  if i in {"a","e","i","o","u"}:
    vogais += 1
  if i in {"0","1","2","3","4","5","6","7","8","9"}:
    digitos += 1
    
#Saida
if vogais > digitos and digitos >= 2 and caracteres >= 8:
  print("OK")
else:
 print("ERRO")
