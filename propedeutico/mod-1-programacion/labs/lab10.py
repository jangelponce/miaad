# Inicializar la suma
suma = 0  # Comenzar la suma en 0

# Usar un bucle while para sumar números
while True:  # Bucle infinito que se detendrá con un break
    numero = float(input("Ingrese un número (0 para terminar): "))  # Solicitar un número
    if numero == 0:  # Verificar si el número es 0
        break  # Salir del bucle si se ingresa 0
    suma += numero  # Sumar el número ingresado a la suma total

# Imprimir el resultado de la suma
print(f"La suma total es: {suma}")  # Mostrar la suma total
