# Condicionales 

print("Promedio Materias.")

nombre = input("Indica tu nombre: ")

nMaterias = int(input("Escriba el numero de materias: "))

suma = 0

for i in range(nMaterias):
  nombreMateria = input("Nombre de la materia: ")
  notaMateria = float(input("Escriba nota: ") )
  suma += notaMateria
  
prom = suma / nMaterias

'''
for i in range(nMaterias):
  print("Materia: ", nombreMateria)
  print("Nota: ", notaMateria)
'''

if prom >= 3:
  print(nombre + " 'Aprobaste' el promedio! siendo: ", prom)
  
elif prom < 3:
  print(nombre + " 'Reprobaste' el promedio, siendo: ", prom)