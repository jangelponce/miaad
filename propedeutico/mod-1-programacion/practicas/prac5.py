# Practica 5. Generador de Tabla de Multiplicar
# Crea un programa que pida al usuario un número y genere la tabla de multiplicar de ese número del 1 al 10.

# Instrucciones:
# 1. Pide al usuario que ingrese un número.
# 2. Usa un bucle for para iterar del 1 al 10 y calcular el producto del número ingresado por cada uno de esos valores.
# 3. Imprime el resultado en un formato legible. (puede emplear algo similar a esta linea: 
# print(f"{numero} x {i} = {resultado}")

# 1. Captura de entradas
number = int(input("Ingresa un número: "))

# 2. Cálculo de la tabla
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")