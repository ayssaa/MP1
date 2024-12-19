#Problema: CPF

#Entrada
cpf = str(input())
carac = [".","-"]

#Saida
cpfcerto = ""
for num in cpf:
  if num not in carac:
    cpfcerto += num
print(cpfcerto)
