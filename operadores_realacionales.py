# Operadores Relacionales

print("Indica dos numeros a comparar... \n")

num_1 = int(input("Indique el número uno: "))
num_2 = int(input("Indique el número dos: \n"))

print("Los numeros a comparar son: ", num_1, " y ", num_2, "\n")

if num_1 == num_2:
  print("Los numeros son iguales.\n")
if num_1 > num_2:
  print("numero uno es mayor que numero dos.")
if num_2 > num_1:
  print("numero dos es mayor que numero uno.")
if num_1 < num_2:
  print("numero uno es menor que numero dos.")
if num_2 < num_1:
  print("numero dos es menor que numero uno\n.")
  
if num_1 >= num_2:
  print("numero uno es mayor igual que numero dos.")
if num_2 >= num_1:
  print("numero dos es mayor igual que numero uno.")
if num_1 <= num_2:
  print("numero dos es mayor igual que numero uno.")
if num_2 <= num_1:
  print("numero uno es mayor igual que numero dos.\n")
if num_1 != num_2:
  print("Los numeros son distintos..")