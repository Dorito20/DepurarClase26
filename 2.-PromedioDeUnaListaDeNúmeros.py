#Objetivo: Comprender la importancia de inicializar correctamente las variables y cómo manejar listas.
#Problema: El siguiente código debería calcular el promedio de una lista de números, pero está dando un error de división por cero.

def calcular_promedio(numeros):

    suma = 0

    for numero in numeros:

        suma += numero

    promedio = suma / len(numeros)

    return promedio



lista_numeros = [10, 20, 30, 40, 50]

print("El promedio es:", calcular_promedio(lista_numeros))

#corregir errores 
def calcular_promedio(numeros):
    if len(numeros) == 0:  # Verificar si la lista está vacía
        return "Error: La lista está vacía, no se puede calcular el promedio."

    suma = 0
    for numero in numeros:
        suma += numero

    promedio = suma / len(numeros)
    return promedio

lista_numeros = [10, 20, 30, 40, 50]
print("El promedio es:", calcular_promedio(lista_numeros))

#Deber:Modifica el código para que, si la lista está vacía, devuelva un mensaje que diga "La lista está vacía" en lugar de intentar calcular el promedio.
def calcular_promedio(numeros):
    if len(numeros) == 0:  # Verificar si la lista está vacía
        return "La lista está vacía"
    
    suma = 0
    for numero in numeros:
        suma += numero

    promedio = suma / len(numeros)
    return promedio

lista_numeros = [10, 20, 30, 40, 50]
print("El promedio es:", calcular_promedio(lista_numeros))
