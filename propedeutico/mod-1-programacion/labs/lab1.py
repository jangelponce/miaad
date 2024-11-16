# Laboratorio: Uso de la función print()

# 1. Imprimir texto simple
print("¡Bienvenido al laboratorio de Python!")  # Imprime un saludo en la consola

# 2. Imprimir variables
nombre = "Angel"  # Definimos una variable con el nombre
edad = 31  # Definimos una variable con la edad
print("Nombre:", nombre)  # Imprime el nombre
print("Edad:", edad)  # Imprime la edad

# 3. Imprimir múltiples variables en una sola línea
print("Nombre:", nombre, "| Edad:", edad)  # Usamos comas para separar las variables

# 4. Usar formato de cadenas
# Método 1: Usar el método format()
print("Hola, {}. Tienes {} años.".format(nombre, edad))  # Imprime usando format()

# Método 2: Usar f-strings (Python 3.6+)
print(f"Hola, {nombre}. Tienes {edad} años.")  # Imprime usando f-strings

# 5. Imprimir una lista
lista_frutas = ["manzana", "banana", "cereza"]  # Definimos una lista de frutas
print("Lista de frutas:", lista_frutas)  # Imprime la lista

# 6. Imprimir un diccionario
diccionario = {"nombre": nombre, "edad": edad, "ciudad": "Juarez"}  # Definimos un diccionario
print("Datos de la persona:", diccionario)  # Imprime el diccionario

# 7. Usar sep y end en print
print("Valor 1", "Valor 2", "Valor 3", sep=" - ")  # Cambia el separador entre elementos
print("Este es el primer mensaje.", end=" ")  # No añade salto de línea
print("y este es el segundo mensaje.")  # Continúa en la misma línea