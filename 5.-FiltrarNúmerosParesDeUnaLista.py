#Objetivo: Practicar la comprensión de listas y la creación de nuevas listas a partir de condiciones.
#Problema: El siguiente código debería filtrar solo los números pares de una lista, pero no está funcionando correctamente.
def filtrar_pares(numeros):

    pares = []

    for numero in numeros:

        if numero % 2 == 0:

            pares.append(numero)

    return pares



lista_numeros = [1, 2, 3, 4, 5, 6]

print("Números pares:", filtrar_pares(lista_numeros))


#corregir errores 
def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

lista_numeros = [1, 2, 3, 4, 5, 6]
print("Números pares:", filtrar_pares(lista_numeros))

#Deber:Asegúrate de que el código funciona correctamente para listas con números positivos, negativos e incluso con ceros.
def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Lista con números positivos
lista_numeros_positivos = [1, 2, 3, 4, 5, 6]
print("Números pares:", filtrar_pares(lista_numeros_positivos))  # Debería imprimir [2, 4, 6]

# Lista con números negativos
lista_numeros_negativos = [-7, -6, -5, -4, -3, -2, -1, 0]
print("Números pares:", filtrar_pares(lista_numeros_negativos))  # Debería imprimir [-6, -4, -2, 0]

# Lista con ceros
lista_numeros_con_cero = [0, 1, -1, 2, -2]
print("Números pares:", filtrar_pares(lista_numeros_con_cero))  # Debería imprimir [0, 2, -2]

# Lista vacía
lista_vacia = []
print("Números pares:", filtrar_pares(lista_vacia))  # Debería imprimir []

# Lista con un solo número impar
lista_un_impar = [1]
print("Números pares:", filtrar_pares(lista_un_impar))  # Debería imprimir []

# Lista con un solo número par
lista_un_par = [4]
print("Números pares:", filtrar_pares(lista_un_par))  # Debería imprimir [4]
