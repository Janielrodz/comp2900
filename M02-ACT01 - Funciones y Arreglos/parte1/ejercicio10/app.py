def contar_apariciones_letra(cadena, letra):
    suma = 0 #Se inicializa la variable 
    for caracter in cadena:
        #condición, el caracter equivale al valor de variable letra
        if caracter == letra: 
            suma += 1 #acumulador, va sumando de 1 en 1 
    return suma

#Se inicializa la función y se le otorgan los valores a los parámetros.
resultado = contar_apariciones_letra(cadena= "extraterrestre", letra= 'e') 
print(f"La letra 'e' aparece {resultado} veces.")