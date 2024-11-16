# Practica 4. Calculador de Impuestos
# Crea un programa que pida al usuario que ingrese su ingreso anual y calcule el impuesto que debe pagar según las siguientes tasas:

# Menos de 10,000: 0%
# De 10,000 a 20,000: 10%
# De 20,001 a 50,000: 20%
# Más de 50,000: 30%
# Instrucciones:
# Pide al usuario que ingrese su ingreso anual.
# Usa if para verificar si el ingreso es un número negativo.
# Usa if-elif-else para determinar el porcentaje de impuesto y calcular el monto a pagar.

# 1. Captura de entradas
income = float(input("Ingresa su ingreso anual: "))

# 2. Verificación de ingreso
if income < 0:
    print("Error: El ingreso no puede ser negativo.")
else:
    # 3. Cálculo del impuesto
    if income < 10000:
        tax = 0
    elif income < 20000:
        tax = 10
    elif income < 50000:
        tax = 20
    else:
        tax = 30
    
    # 4. Cálculo del monto a pagar
    amount_to_pay = income * tax / 100
    
    # 5. Impresión del resultado
    print("El monto a pagar por el impuesto es:", amount_to_pay)