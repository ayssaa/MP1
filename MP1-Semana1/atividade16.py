#Problema: minutos para horas

#Entrada
minutos = int(input ())

#Calculando total em hora
totalhora = (minutos // 60)
totalminuto = (minutos % 60)

#Tempo total em horas
print(str(minutos) + "min = " + str(totalhora) + "h" + str(totalminuto) + "min")