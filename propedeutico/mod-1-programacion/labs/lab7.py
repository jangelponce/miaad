# Solicitar al usuario que ingrese un número del 1 al 7
dia = int(input("Ingrese un número del 1 al 7 para el día de la semana: "))

# Verificar si el número está fuera del rango válido (1 a 7)
if dia < 1 or dia > 7:
    print("Número no válido. Debe estar entre 1 y 7.")
# Si el número es 6 o 7, es fin de semana
elif dia == 6 or dia == 7:
    print("Es fin de semana.")
# Si el número está entre 1 y 5, es un día de la semana
elif dia >= 1 and dia <= 5:
    print("Es un día de la semana.")
