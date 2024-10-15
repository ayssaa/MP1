#Problema: Tempo numa prova

#Entrada
hinicio = int(input ()) #hora de inicio
minicio = int(input ()) #minuto de inicio
hfinal = int(input ()) #hora de termino
mfinal = int(input ()) #minuto de termino

#Quantos minutos demorei?
horastotal = hfinal - hinicio
minutototal = mfinal - minicio
tempot = (horastotal * 60) + minutototal

#tempo em minutos
print(tempot)