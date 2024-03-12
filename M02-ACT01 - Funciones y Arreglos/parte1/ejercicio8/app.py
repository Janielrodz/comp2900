def contar_vocales(cadena): #Función
    
    i = 0 #Se crea la variable para el contador
    
    for vocal in cadena: # Ciclo for y se crea la variable vocal
        if vocal.lower() in "aeiou": #condición y se usa el metodo lower.
            i = i + 1 # Contador de 1 en 1.
    return i

palabraUsuario = input("Ingrese la palabra que desea verificar: ") #Consulta al usuario

resultado = contar_vocales(palabraUsuario) #Se le otorga el resultado a la variable.

if resultado == 1: #Condicion, si hay 1 vocal imprime un mensaje singular.
    print(f"La palabra ({palabraUsuario}) tiene {resultado} vocal.")

else: #De lo contrario, si hay más de 1 vocal imprime un mensaje plural.
    print(f"La palabra ({palabraUsuario}) tiene {resultado} vocales.")    

