# Practica 1. Tipos de variables en Python
# Descripción: Declara diferentes tipos de variables en Python y muestra su valor y tipo.
# 
# Instrucciones:
# 
# 1. Crea una variable entera, una variable de punto flotante, una variable de texto y una variable booleana.
# 2. Usa print() para mostrar el valor y el tipo de cada variable.
# 3. Envia tu codigo .py y una captura de pantalla de los resultados que hayas obtenido en tu codigo

# Definicion de variables entera, flotante, cadena y booleano
age = 10
price = 20.5
name = "Angel"
registered = True

# Impresión de variables
print("Age:", age)
print("Price:", price)
print("Name:", name)
print("Registered:", registered)

# Impresión de variables con formato
print("Age: {:d}".format(age))
print("Price: {:.2f}".format(price))
print("Name: {!s}".format(name))
print("Registered: {:b}".format(registered))

