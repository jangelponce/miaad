# Practica 6. Calculadora de Áreas


# Crea un programa que defina funciones para calcular el área de un círculo, un rectángulo y un triángulo. Luego, permite al usuario elegir qué figura quiere calcular y pide los parámetros necesarios.


# Instrucciones:

# 1. Define una función area_circulo(radio) que calcule el área de un círculo.
# 2. Define una función area_rectangulo(base, altura) que calcule el área de un rectángulo.
# 3. Define una función area_triangulo(base, altura) que calcule el área de un triángulo.
# 4. Permite al usuario seleccionar la figura de la que quiere calcular el área e ingresar los valores necesarios. Diseña un pequeño menu de seleccion del tipo de area que desea calcular
# 5. Muestra el resultado del cálculo.

# 1. Definición de funciones
def area_circulo(radio):
    return 3.14 * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return 0.5 * base * altura

# 2. Captura de entradas
tipo_figura = input("Selecciona la figura de la que quieres calcular el área: ")
if tipo_figura == "círculo":
    radio = float(input("Ingresa el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El área del círculo es: {area}")
elif tipo_figura == "rectángulo":
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    area = area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area}")
elif tipo_figura == "triángulo":
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area = area_triangulo(base, altura)
    print(f"El área del triángulo es: {area}")
else:  # Si el usuario ingresa una opción no válida
    print("Opción no válida.")