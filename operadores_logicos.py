# Operadores Logicos.

# Conjucion 
print("Conjuncion (and)")

n1 = int(input("Escriba un numero > 2 & <= 5: "))

if n1 > 2 and n1 <= 5:
  print("El numero ", n1, " cumple con la condicion.\n")
else:
  print("El numero ", n1, " no cumple con la condicion.\n")

print("Disyuncion (or)")

palabra = input("Para cumplir con la condicion escriba 'si' o 'yes': ")
palabra = palabra.lower()

if palabra == "si" or palabra == "yes":
  print("la condicion se ha cumplido.\n")
else:
  print("no la condicion se ha cumplido.\n")

print("negacion (not)")
num_uno = int(input("introduce un numero igual a 5: "))

if not num_uno == 5:
  print("El numero no es igual a 5 es diferente de 5 y si cumple la condicion ")
else:
  print("El numero es igual a 5 es diferente de 5 y no cumple la condicion ")

