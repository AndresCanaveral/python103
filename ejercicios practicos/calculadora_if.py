# Calculadora con una sola variable

print("Calculadora con una sola variable.")

print("******************")
print("* MENU PRINCIPAL *")
print("****************** \n")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division entera")
print("6. Exponente")
print("7. Modulo o resto \n")


opc = int(input("Escoja una opcion: "))

if opc == 1:
  print("Elegiste suma \n")
  n1 = int(input("Indique primer numero a sumar: "))
  n1 += int(input("Indique segundo numero a sumar: "))
  print("El resultado de la suma es ", n1)
  
elif opc == 2:
  print("Elegiste resta \n")
  n1 = int(input("Indique primer numero a restar: "))
  n1 -= int(input("Indique segundo numero a restar: "))
  print("El resultado de la resta es ", n1)

elif opc == 3:
  print("Elegiste multiplicacion \n")
  n1 = int(input("Indique primer numero a multiplicar: "))
  n1 *= int(input("Indique segundo numero a multiplicar: "))
  print("El resultado de la multiplicacion es ", n1)

elif opc == 4:
  print("Elegiste division \n")
  n1 = float(input("Indique primer numero a dividir: "))
  n1 /= float(input("Indique segundo numero a dividir: "))
  print("El resultado de la division es ", round(n1, 2))

elif opc == 5:
  print("Elegiste division entera \n")
  n1 = int(input("Indique primer numero a dividir: "))
  n1 //= int(input("Indique segundo numero a dividir: "))
  print("El resultado de la division es ", n1)

elif opc == 6:
  print("Elegiste exponente \n")
  n1 = int(input("Indique primer numero: "))
  n1 **= int(input("Indique segundo numero: "))
  print("El resultado del exponente es ", n1)

elif opc == 7:
  print("Elegiste modulo o resto \n")
  n1 = int(input("Indique primer numero a sumar: "))
  n1 %= int(input("Indique segundo numero a sumar: "))
  print("El resultado del modulo o resto es ", n1)
  
else:
  print("Esta opcion no existe")

  