## Bucle o ciclo while
# Sucesion Fibonacci
'''

num_uno, num_dos = 0, 1

while num_dos <= 1597:
  print(num_uno, num_dos, end=" ")
  num_uno = num_uno + num_dos
  num_dos = num_uno + num_dos
  
'''

# Sentencia Break

print("While con la sentencia break \n")

contador = 0

while contador < 10:
  contador += 1

  if contador == 5:
    break
  print("valor actual de la variable ", contador)

