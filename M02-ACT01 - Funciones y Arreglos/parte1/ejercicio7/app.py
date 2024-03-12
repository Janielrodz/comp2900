def es_numero_entero(cadena): #Funcion
    if str(cadena).isdigit(): #Condicion, se usa la funcion .isdigit, la funcion determina cuando el numero es entero.
        print("El valor de la cadena es un numero entero.")

    else: #De lo contrario, si el numero no es entero imprime el siguiente mensaje:
        print("El valor de la cadena NO es un numero entero.")

cadena = str(input("Ingrese el numero que desea validar: ")) #Consulta al usuario el numero que desea validar.
es_numero_entero(cadena) #Se llama a la función.
        