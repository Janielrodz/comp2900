def invertir_cadena(cadena):
    print(f"Cadena original: {cadena}")
    #Se crea la variable que almacenará la cadena invertida
    cadena_invertida = "" 
    #Se crea un ciclo e invierte la cadena
    for caracter in cadena[::-1]:
        cadena_invertida += caracter
    return cadena_invertida

resultado = invertir_cadena("Hola") #Se inicializa la función
print(f"La cadena invertida es: {resultado}") #Salida
