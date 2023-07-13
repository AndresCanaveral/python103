# Numero mayor

print("*" * 40)
print("Numero mayor.")
print("*" * 40)

n1 = int(input("Indique numero 1: "))
n2 = int(input("Indique numero 2: "))
n3 = int(input("Indique numero 3: "))

if n1 > n2 and n1 > n3:
  print("Numero ", n1, "Es mayor que ", n2, "y ",n3)

elif n2 > n3:
  print("Numero ", n2, "Es mayor que ", n1, "y ",n3)
  
else:
  print("Numero ", n3, "Es mayor que ", n1, "y ",n2)
