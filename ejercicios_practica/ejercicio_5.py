# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :

letras_palabra_1 = palabra_1[0:3]
print(letras_palabra_1)


# De la segunda palabra tome las primeras dos letras, utilice el operador :

letras_palabra_2 = palabra_2[:2]
print(letras_palabra_2)

# Formar una nueva palabra con los recortes solicitados

nueva_palabra = letras_palabra_1 + letras_palabra_2
print(nueva_palabra)

# Imprima en pantalla los resultados
