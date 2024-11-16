# Laboratorio sobre entradas de usuario, conversión de tipos y operaciones matemáticas

# Parte 1: Introducción a input() y tipos de datos

# Ejercicio 1: Captura de un número entero e impresión
edad_str = input("Por favor, ingresa tu edad: ")  # input() captura como texto
edad = int(edad_str)  # Convertimos la cadena a un número entero
print("Tu edad es:", edad)  # Mostramos la edad como un número entero


# Ejercicio 2: Captura de un número decimal e impresión
numero_str = input("Ingresa un número decimal: ")  # input() captura como texto
numero = float(numero_str)  # Convertimos la cadena a un número flotante
resultado = numero + 5  # Realizamos una operación (sumar 5 al número ingresado)
print("El resultado de sumar 5 a tu número es:", resultado)  # Mostramos el resultado


# Parte 2: Validación de entradas

# Ejercicio 3: Validación para asegurarse que el usuario ingresa un número entero
try:
    numero_str = input("Ingresa un número entero: ")  # input() captura como texto
    numero = int(numero_str)  # Intentamos convertir la cadena a un entero
    print("Número ingresado correctamente:", numero)  # Mostramos el número ingresado
except ValueError:  # Si el usuario no ingresa un número entero válido
    print("Error: Debes ingresar un número entero válido.")  # Mensaje de error


# Parte 3: Operaciones matemáticas

# Ejercicio 4: Realizar operaciones con números enteros y flotantes
num1_str = input("Ingresa un número entero: ")
num2_str = input("Ingresa un número decimal: ")

num1 = int(num1_str)  # Convertimos el primer número a entero
num2 = float(num2_str)  # Convertimos el segundo número a flotante

# Realizamos algunas operaciones matemáticas
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2 if num2 != 0 else "Error: No se puede dividir entre cero."

# Mostramos los resultados de las operaciones
print("La suma de los dos números es:", suma)
print("La resta de los dos números es:", resta)
print("El producto de los dos números es:", producto)
print("La división de los dos números es:", division)


# Parte 4: Calculadora interactiva simple

# Ejercicio 5: Calculadora simple
print("\nCalculadora simple")
# Capturamos dos números
num1_str = input("Ingresa el primer número: ")
num2_str = input("Ingresa el segundo número: ")

# Convertimos las entradas a números flotantes
num1 = float(num1_str)
num2 = float(num2_str)

# Mostramos un menú de operaciones disponibles
print("Operaciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Capturamos la opción elegida por el usuario
operacion = input("Elige una operación (1/2/3/4): ")

# Dependiendo de la opción, realizamos la operación correspondiente
if operacion == "1":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif operacion == "2":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif operacion == "3":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif operacion == "4":
    if num2 != 0:  # Comprobamos que no haya división por cero
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")  # Si el usuario ingresa una opción no válida

