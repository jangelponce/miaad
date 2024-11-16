print('Hola, en este laboratorio, observaras como se definen variables en python, asi como el uso basico del print\n')
print('*****************************************************************************************')

##Recuerda, que todo las instrucciones o texto que esten precedidos de un # significan comentarios y python no los interpretará


# 1. Crear Variables
#para las variables del tipo numerica, enteras o flotantes, solo es necesario colocar el nombre de la variable, el simbolo de igual y el valor que deseas asignarle a la variable

entero = 10 #esta es una variable entera
flotante = 20.5

#*******************************************************************************
#Para el caso de una cadena de caracteres, se define de igual forma la variable precedeida de un = y luego entre comillas ('' o "") la cadena que se desea colocar

cadena = "Hola, Python"

#*******************************************************************************
#Las listas, se definene entre [] y como puedes observar, estas pueden contaner diferentes tipos de valores, en este caso se tiene un dato entero, un cadena de caracteres, un boleano y un flotante 

lista = [1, "texto", True, 1.245]

#*******************************************************************************

#Los diccionarions contienen pares clave-valor. Aquí, la clave "nombre" tiene el valor "Angel" y la clave "edad" tiene el valor 31. Los diccionarios son útiles para almacenar datos relacionados.
diccionario = {"nombre": "Angel", "edad": 31}


#Finalmente, se utiliza la función print para mostrar el valor de la variable y su tipo. type(nombredelavariable) devuelve el tipo de la variable.
#La estructura para este caso es la siguiente
    #print("Texto a imprimir en pantalla", variable a imprimir en pantalla, "Texto:", type(nombredevariable))

# Imprimir valores y tipos

print("Entero:", entero, "Tipo:", type(entero))
print("Flotante:", flotante, "Tipo:", type(flotante))
print("Cadena:", cadena, "Tipo:", type(cadena))
print("Lista:", lista, "Tipo:", type(lista))
print("Diccionario:", diccionario, "Tipo:", type(diccionario))