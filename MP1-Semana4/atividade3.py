#Problema: Dado um valor disponivel, permitir adição de itens sem estourar o limite

#Entrada
valor_disponivel = int(input())
valor_itens = 0
numero_itens = 0

while True:
  item = int(input())
  if valor_itens + item <= valor_disponivel:
    valor_itens += item
    numero_itens += 1
  else:
    break

#Saida
print("Número de itens", numero_itens)
print("Saldo:", "%.2f" % (valor_disponivel - valor_itens))
