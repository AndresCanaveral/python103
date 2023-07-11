# Condicionales multiples Condicionales anidadas
print("*" * 40)
print("Convertidor de numeros a letras. \n")
print("Presiona 1 para convertir de numero a palabra ")
print("Presiona 2 para convertir de palabra a numero \n")

opc = int(input("Indica la opcion: "))
print("*" * 40)

if opc == 1:
  print("\nConversor de numero a palabra \n")
  
  opcion_uno = int(input("Cual es el numero que quieres convertir a palabra?: "))
  if opcion_uno == 1:
    print("El numero es 'tres'. ")
  elif opcion_uno == 2:
    print("El numero es 'dos'. ")
  elif opcion_uno == 3:
    print("El numero es 'tres'. ")
  elif opcion_uno == 4:
    print("El numero es 'cuatro'. ")
  elif opcion_uno == 5:
    print("El numero es 'cinco'. ")
  else: 
    print("El numero seleccionado no está permitido")
    
elif opc == 2:
  print("\nConversor de palabra a numero \n")
  
  opcion_dos = input("Cual es la letra que quieres convertir a numero? : ")
  opcion_dos = opcion_dos.lower()
  
  if opcion_dos == "uno":
    print("El numero es '1'. ")
  elif opcion_dos == "dos":
    print("El numero es '2'. ")
  elif opcion_dos == "tres":
    print("El numero es '3'. ")
  elif opcion_dos == "cuatro":
    print("El numero es '4'. ")
  elif opcion_dos == "cinco":
    print("El numero es '5'. ")
  else:
    print("el numero seleccionado no esta registrado")
  
else:
  print("Opcion no disponible.")


