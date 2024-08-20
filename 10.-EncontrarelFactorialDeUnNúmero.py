#Objetivo: Practicar la implementación de algoritmos matemáticos en Python.

#Problema: Este código debería calcular el factorial de un número (el producto de todos los números enteros positivos hasta ese número), pero no produce el resultado correcto.

def factorial(n):

    resultado = 1

    for i in range(1, n + 1):

        resultado *= i

    return resultado



numero = 5

print("Factorial de", numero, "es:", factorial(numero))

#corregir errores 
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = 5
print("Factorial de", numero, "es:", factorial(numero))

# Casos de prueba adicionales
print("Factorial de 0 es:", factorial(0))  # Debería imprimir 1
print("Factorial de 1 es:", factorial(1))  # Debería imprimir 1

#Deber: Asegúrate de que el código funcione correctamente para calcular el factorial de cualquier número entero positivo.
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Casos de prueba
print("Factorial de 0 es:", factorial(0))  # Debería imprimir 1
print("Factorial de 1 es:", factorial(1))  # Debería imprimir 1
print("Factorial de 5 es:", factorial(5))  # Debería imprimir 120
print("Factorial de 10 es:", factorial(10))  # Debería imprimir 3628800
