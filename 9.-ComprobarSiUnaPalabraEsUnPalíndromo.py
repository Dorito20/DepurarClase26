#Objetivo: Entender cómo manipular cadenas y realizar comparaciones de manera eficiente.
#Problema: Este código debería comprobar si una palabra es un palíndromo (una palabra que se lee igual de adelante hacia atrás), pero no está funcionando correctamente para ciertas palabras.

def es_palindromo(palabra):

    palabra_invertida = ""

    for i in range(len(palabra)):

        palabra_invertida += palabra[i-1]

    return palabra == palabra_invertida



palabra = "radar"

print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")

#corregir errores 
def es_palindromo(palabra):
    # Construir la palabra invertida usando slicing
    palabra_invertida = palabra[::-1]
    
    # Comparar la palabra original con la invertida
    return palabra == palabra_invertida

# Prueba con un ejemplo
palabra = "radar"
print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")

#Deber: Corrige el código para que pueda identificar correctamente si una palabra es un palíndromo.
def es_palindromo(palabra):
    palabra_invertida = ""
    
    # Iterar desde el final de la palabra hasta el principio
    for i in range(len(palabra) - 1, -1, -1):
        palabra_invertida += palabra[i]
    
    return palabra == palabra_invertida

# Prueba con un ejemplo
palabra = "radar"
print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")

