# Laboratorio sobre funciones en Python

# Parte 1: Definición y uso básico de funciones

# Ejercicio 1: Función sin parámetros
print("Ejercicio 1: Función sin parámetros")
def saludo():
    print("¡Bienvenidos al laboratorio de funciones en Python!")
saludo()  # Llamamos a la función

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 2: Función con un parámetro
print("Ejercicio 2: Función con un parámetro")
def saludo_personalizado(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al laboratorio de funciones.")
saludo_personalizado("Juan")  # Llamamos a la función pasando el argumento "Juan"

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 3: Función con múltiples parámetros
print("Ejercicio 3: Función con múltiples parámetros")
def saludo_con_edad(nombre, edad):
    print(f"¡Hola, {nombre}! Tienes {edad} años.")
saludo_con_edad("Carlos", 25)  # Llamamos a la función pasando dos argumentos: nombre y edad

print("\n")  # Salto de línea para separar los ejercicios

# Parte 2: Funciones que devuelven valores

# Ejercicio 4: Función que devuelve un valor
print("Ejercicio 4: Función que devuelve un valor")
def suma(a, b):
    return a + b

resultado = suma(3, 5)  # Llamamos a la función y almacenamos el resultado
print("La suma es:", resultado)  # Mostramos el resultado

print("\n")  # Salto de línea para separar los ejercicios

# Ejercicio 5: Función con valor predeterminado
print("Ejercicio 5: Función con valores predeterminados")
def saludo_edad(nombre, edad=30):  # Edad tiene un valor predeterminado de 30
    print(f"¡Hola, {nombre}! Tienes {edad} años.")
saludo_edad("Ana", 22)  # Llamamos con dos argumentos
saludo_edad("Luis")  # Llamamos solo con el nombre, usando el valor predeterminado para edad

print("\n")  # Salto de línea para separar los ejercicios

# Parte 3: Funciones con número variable de argumentos

# Ejercicio 6: Función con *args
print("Ejercicio 6: Función con número variable de argumentos")
def imprimir_nombres(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")
        
# Llamamos a la función con varios argumentos
imprimir_nombres("Carlos", "Juan", "Ana")

print("\n")  # Salto de línea para separar los ejercicios

# Parte 4: Funciones que realizan múltiples operaciones

# Ejercicio 7: Función que devuelve múltiples valores
print("Ejercicio 7: Función que devuelve múltiples valores")
def operaciones_matematicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return suma, resta, multiplicacion, division

# Llamamos a la función con dos números y desempaquetamos los resultados
s, r, m, d = operaciones_matematicas(10, 5)

# Mostramos los resultados de las operaciones
print("Suma:", s)  # 15
print("Resta:", r)  # 5
print("Multiplicación:", m)  # 50
print("División:", d)  # 2.0

