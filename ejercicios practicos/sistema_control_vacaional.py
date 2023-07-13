# Ejercicio practico N°1

print("*" * 40)
print("Sistema de Control Vacacional.")
print("*" * 40)

name = input("Escriba nombre: ")
clave = int(input("Escriba clave: "))
anio = int(input("Escriba años: "))

if clave == 1:
  if anio == 1:
    print("el empleado", name, "6 dias de vacaiones. ")
  elif anio >= 2 and anio <= 6:
    print("el empleado", name,"14 dias de vacaciones. ")
  elif anio >= 7:
    print("el empleado", name,"20 dias de vacaciones. ")
  else:
    print("el empleado", name,"Sin derecho a vacaciones. ")
    
elif clave == 2:
  if anio == 1:
    print("el empleado", name,"7 dias de vacaiones. ")
  elif anio >= 2 and anio <= 6:
    print("el empleado", name,"15 dias de vacaciones. ")
  elif anio >= 7:
    print("el empleado", name,"22 dias de vacaciones. ")
  else:
    print("el empleado", name,"Sin derecho a vacaciones. ")
    
elif clave == 3:
  if anio == 1:
    print("el empleado", name,"10 dias de vacaiones. ")
  elif anio >= 2 and anio <= 6:
    print("el empleado", name,"20 dias de vacaciones. ")
  elif anio >= 7:
    print("el empleado", name,"30 dias de vacaciones. ")
  else:
    print("el empleado", name,"Sin derecho a vacaciones. ")

else:
  print("la clave no existe. ")