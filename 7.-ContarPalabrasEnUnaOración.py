#Objetivo: Aprender a manejar cadenas y listas en Python.
#Problema: Este código debería contar el número de palabras en una oración, pero no funciona como se espera.
def contar_palabras(oracion):

    palabras = oracion.split(",")

    return len(palabras)



oracion = "Este es un ejemplo de oración"

print("Número de palabras:", contar_palabras(oracion))

#corregir errores 
#Deber: Corrige el código para que cuente el número de palabras en la oración correctamente.
def contar_palabras(oracion):
    palabras = oracion.split()  # Usar el separador por defecto, que es el espacio
    return len(palabras)

oracion = "Este es un ejemplo de oración"
print("Número de palabras:", contar_palabras(oracion))  # Debería imprimir 6
