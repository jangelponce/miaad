# Laboratorio: Operaciones Aritméticas Básicas

# 1. Solicitar dos números al usuario
numero1 = input("Ingresa el primer número: ")  # Captura la entrada del usuario
numero2 = input("Ingresa el segundo número: ")  # Captura la entrada del usuario

# 2. Convertir las entradas a flotantes
numero1 = float(numero1)  # Convierte el primer número a flotante
numero2 = float(numero2)  # Convierte el segundo número a flotante

# 3. Realizar operaciones aritméticas
suma = numero1 + numero2  # Suma
resta = numero1 - numero2  # Resta
multiplicacion = numero1 * numero2  # Multiplicación
division = numero1 / numero2  # División (asumiendo que numero2 no es cero)

# 4. Imprimir los resultados
print("La suma de", numero1, "y", numero2, "es:", suma)  # Imprime la suma
print("La resta de", numero1, "y", numero2, "es:", resta)  # Imprime la resta
print("La multiplicación de", numero1, "y", numero2, "es:", multiplicacion)  # Imprime la multiplicación
print("La división de", numero1, "y", numero2, "es:", division)  # Imprime la división
