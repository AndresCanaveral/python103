# Condicionales 

print("Promedio de 3 materias.")

nombre = input("Indica tu nombre: ")

mate = float(input("Nota de Matematicas: "))
quim = float(input("Nota de Quimica: "))
biol = float(input("Nota de Biologia: "))

prom = (mate + quim + biol) / 3
prom = int(prom)

if prom >= 3:
  print(nombre + " 'Aprobaste' el promedio! siendo: ", prom)

elif prom < 3:
  print(nombre + " 'Reprobaste' el promedio, siendo: ", prom)




