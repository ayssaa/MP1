#Problema: Proporções

#Entrada
qntlista1 = int(input ())
qntlista2 = int(input ())
qntlista3 = int(input ())
qntlista4 = int(input ())
rlvlista1 = int(input ())
rlvlista2 = int(input ())
rlvlista3 = int(input ())
rlvlista4 = int(input ())

#Calculando a porcentagem
porclista1 = (rlvlista1 / qntlista1) * 100
porclista2 = (rlvlista2 / qntlista2) * 100
porclista3 = (rlvlista3 / qntlista3) * 100
porclista4 = (rlvlista4 / qntlista4) * 100

#Porcentagem
print("%.1f" % porclista1)
print("%.1f" % porclista2)
print("%.1f" % porclista3)
print("%.1f" % porclista4)