# Solicitar al usuario que ingrese un año
anio = int(input("Ingrese un año: "))  # Se convierte la entrada a tipo entero

# Verificar si el año es bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):  # Comprueba las condiciones para ser bisiesto
    print(f"El año {anio} es bisiesto.")  # Imprime si el año es bisiesto
else:  # Si no cumple las condiciones para ser bisiesto
    print(f"El año {anio} no es bisiesto.")  # Imprime si el año no es bisiesto