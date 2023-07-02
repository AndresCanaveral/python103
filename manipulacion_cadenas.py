# Asignacion
print("*" * 40)
print("Asignacion")
mensaje = "Hola"
mensaje += " "
mensaje += "Andres"
print(mensaje)


# Concatenacion 
print("*" * 40)
print("Concatenacion")
mensaje = "Hola"
espacio = " "
nombre = "Andres"
print(mensaje + espacio + nombre)

# Concatenacion con caracter numerico.
print("*" * 40)
print("Suma de 5 + 6")
n1 = 5
n2 = 6
resultado = n1 + n2
resultado = str(resultado)
print("La suma es: " + resultado)


# Busqueda de caracteres
print("*" * 40)
print("Busqueda")
mensaje = "Hola Andres"
buscar_subcadena = mensaje.find("Andres") # Muestra la pocisión en la que se encuentra el inicio del string.
print(buscar_subcadena)

# La extraccion
print("*" * 40)
print("Busqueda")
mensaje = "Hola Andres"
extraer_subcadena = mensaje[1:9] # Se está indicando mostrar lo que hay a partir de la poscion 1 y lo que hay antes de las posicion 9 (1 > x < 9)
print(extraer_subcadena)




