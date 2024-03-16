def invertir_orden(): #Funcion
    arreglo =[10, 15, 20, 25, 30] #Arreglo
    #Imprime el arreglo original.
    print(f"Arreglo original: {arreglo}") 

    #Se crea una lista vacía para almacenar el arreglo invertido
    arreglo_invertido = []
    
    #Se crea un ciclo para poder invertir el arreglo.
    for i in range(len(arreglo) -1, -1, -1):
        arreglo_invertido.append(arreglo[i])

    return arreglo_invertido #Devuelve el arreglo invertido

#Se le otorga el valor de la función a la variable.
resultado = invertir_orden() 
print(f"Arreglo invertido: {resultado}") #salida