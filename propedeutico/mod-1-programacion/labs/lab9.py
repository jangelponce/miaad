# Laboratorio sobre el uso del bucle 'for' en Python

# Parte 1: Introducción al bucle 'for'

# Ejercicio 1: Iterar sobre una lista
print("Ejercicio 1: Iterar sobre una lista")
# Creamos una lista de números
numeros = [1, 2, 3, 4, 5]

# Usamos un bucle 'for' para imprimir cada número de la lista
for numero in numeros:
    print("Número:", numero)

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 2: Iterar sobre una tupla
print("Ejercicio 2: Iterar sobre una tupla")
# Creamos una tupla con días de la semana
dias = ("lunes", "martes", "miércoles", "jueves", "viernes")

# Usamos un bucle 'for' para imprimir cada día de la tupla
for dia in dias:
    print("Día de la semana:", dia)

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 3: Iterar sobre un diccionario
print("Ejercicio 3: Iterar sobre un diccionario")
# Creamos un diccionario con nombres y edades
personas = {"Ana": 25, "Luis": 30, "Carlos": 35}

# Usamos un bucle 'for' para imprimir las claves y los valores del diccionario
for nombre, edad in personas.items():
    print(f"{nombre} tiene {edad} años")

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 4: Iterar sobre un conjunto (set)
print("Ejercicio 4: Iterar sobre un conjunto")
# Creamos un conjunto con números
numeros_set = {10, 20, 30, 40, 50}

# Usamos un bucle 'for' para imprimir cada número del conjunto
for numero in numeros_set:
    print("Número en conjunto:", numero)

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 5: Usar 'for' con un rango de números
print("Ejercicio 5: Usar 'for' con un rango de números")
# Usamos un bucle 'for' para iterar sobre un rango de 1 a 5
for i in range(1, 6):
    print("Número en el rango:", i)

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 6: Sumar todos los elementos de una lista
print("Ejercicio 6: Sumar todos los elementos de una lista")
# Creamos una lista de números
numeros_lista = [1, 2, 3, 4, 5]

# Inicializamos una variable para almacenar la suma
suma = 0

# Usamos un bucle 'for' para sumar todos los números de la lista
for numero in numeros_lista:
    suma += numero  # Se suma cada número al total

# Mostramos el resultado
print("La suma de los números de la lista es:", suma)

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 7: Generar una secuencia de números con 'range()' y 'for'
print("Ejercicio 7: Generar una secuencia de números con 'range()' y 'for'")
# Usamos un bucle 'for' con 'range()' para generar y mostrar los números del 1 al 10
for i in range(1, 11):
    print("Número en la secuencia:", i)
