#Objetivo: Practicar la manipulación de listas y la comparación de elementos.
#Problema: Este código debería encontrar el valor máximo en una lista de números, pero devuelve resultados incorrectos.
def encontrar_maximo(numeros):

    maximo = 0

    for numero in numeros:

        if numero > maximo:

            maximo = numero

    return maximo



lista_numeros = [-10, -20, -30, -5, -15]

print("El valor máximo es:", encontrar_maximo(lista_numeros))

#corregir errores 
def encontrar_maximo(numeros):
    # Asegúrate de que la lista no esté vacía antes de proceder
    if not numeros:
        raise ValueError("La lista no puede estar vacía")

    maximo = numeros[0]  # Inicializa maximo con el primer valor de la lista

    for numero in numeros:
        if numero > maximo:
            maximo = numero

    return maximo

lista_numeros = [-10, -20, -30, -5, -15]

print("El valor máximo es:", encontrar_maximo(lista_numeros))

#Deber: Modifica el código para que funcione con cualquier lista, incluyendo listas con solo números negativos.
def encontrar_maximo(numeros):
    # Asegúrate de que la lista no esté vacía antes de proceder
    if not numeros:
        raise ValueError("La lista no puede estar vacía")

    maximo = numeros[0]  # Inicializa maximo con el primer valor de la lista

    for numero in numeros:
        if numero > maximo:
            maximo = numero

    return maximo

lista_numeros = [-10, -20, -30, -5, -15]

print("El valor máximo es:", encontrar_maximo(lista_numeros))
