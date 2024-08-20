#Objetivo: Aprender a identificar y corregir errores en operaciones básicas con listas.
#Problema: El siguiente código debería sumar todos los números en una lista, pero está produciendo un error.

def sumar_lista(numeros):

    suma = 0

    for i in range(len(numeros) + 1):

        suma += numeros[i]

    return suma



lista_numeros = [1, 2, 3, 4, 5]

print("La suma es:", sumar_lista(lista_numeros))

#corregir errores 
def sumar_lista(numeros):
    suma = 0
    # Ajustamos el rango para evitar índice fuera de rango
    for i in range(len(numeros)):
        suma += numeros[i]
    return suma

lista_numeros = [1, 2, 3, 4, 5]
print("La suma es:", sumar_lista(lista_numeros))


#Deber: Modifica el código para que funcione correctamente y suma todos los elementos de la lista sin errores.
def sumar_lista(numeros):
    suma = 0
    for i in range(len(numeros)):
        suma += numeros[i]
    return suma

lista_numeros = [1, 2, 3, 4, 5]
print("La suma es:", sumar_lista(lista_numeros))
