#Problema: CPF
#Entrada
cpf_normal = str(input())
cpf_certo = cpf_normal.replace(".","").replace("-","")
contando = int(0)
caractere_invalido = int(0)

#Verificando caracteres errados + quantidade de caracteres
for i in cpf_certo:
  contando += 1
  if i not in {"0","1","2","3","4","5","6","7","8","9"}:
    caractere_invalido += 1

#Imprimindo resposta de acordo com as variaveis
if caractere_invalido >= 1:
  if contando != 11:
    print("ENCODING ERROR")
    print("SIZE ERROR")
  else:
    print("ENCODING ERROR")
elif contando != 11:
  print("SIZE ERROR")
else:
  print(cpf_certo)

# Sei que fiz gambiarra, mas só consegui pensar nessa solução :(