#Objetivo: Practicar la combinación de elementos de una lista en una sola cadena.
#Problema: El siguiente código debería combinar todas las cadenas de una lista en una sola cadena, separadas por un espacio, pero está agregando un espacio extra al final.

def combinar_cadenas(lista):

    cadena = ""

    for palabra in lista:

        cadena += palabra + " "

    return cadena



lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]

print("Cadena combinada:", combinar_cadenas(lista_cadenas))
                        
#corregir errores 
def combinar_cadenas(lista):
    return " ".join(lista)

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]

print("Cadena combinada:", combinar_cadenas(lista_cadenas))

#Deber: Corrige el código para que la cadena combinada no tenga un espacio extra al final.
def combinar_cadenas(lista):
    if not lista:
        return ""
    
    cadena = lista[0]
    for palabra in lista[1:]:
        cadena += " " + palabra

    return cadena

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]

print("Cadena combinada:", combinar_cadenas(lista_cadenas))


