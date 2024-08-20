#Objetivo: Mejorar la comprensión de cadenas y su manipulación en Python.
#Problema: Este código debería invertir una cadena (es decir, escribirla al revés), pero produce un resultado incorrecto.
def invertir_cadena(cadena):

    invertida = ""

    for i in range(len(cadena)):

        invertida += cadena[i-1]

    return invertida



cadena = "Python"

print("Cadena invertida:", invertir_cadena(cadena))
            
#corregir errores 
def invertir_cadena(cadena):
    invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        invertida += cadena[i]
    return invertida

cadena = "Python"
print("Cadena invertida:", invertir_cadena(cadena))  # Debería imprimir "nohtyP"

#Deber:Corrige el código para que invierta correctamente cualquier cadena.
def invertir_cadena(cadena):
    invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        invertida += cadena[i]
    return invertida

cadena = "Python"
print("Cadena invertida:", invertir_cadena(cadena))  # Debería imprimir "nohtyP"
