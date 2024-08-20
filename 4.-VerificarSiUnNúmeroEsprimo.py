#Objetivo: Desarrollar habilidades para manejar algoritmos más complejos y optimizar la eficiencia del código.
#Problema: Este código debería verificar si un número es primo (un número mayor que 1 que solo es divisible por 1 y por sí mismo), pero está marcando números no primos como primos.

def es_primo(n):

    if n <= 1:

        return False

    for i in range(2, n):

        if n % i == 0:

            return False

    return True



numero = 29

print(f"¿El número {numero} es primo? {es_primo(numero)}")

#corregir errores 
import math

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numero = 29
print(f"¿El número {numero} es primo? {es_primo(numero)}")

#Deber:Optimiza el código para que se detenga cuando sea evidente que el número no es primo, en lugar de recorrer todos los números hasta
import math

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

numero = 29
print(f"¿El número {numero} es primo? {es_primo(numero)}")




