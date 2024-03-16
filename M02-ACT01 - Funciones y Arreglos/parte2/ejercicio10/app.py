def rotar_elementos(arreglo, rotacion):
    #Se mide el largo del arreglo
    longitud = len(arreglo) 
    rotacion = rotacion % longitud  # Procedimiento

    print(f"Arreglo original: {arreglo}")
    
    for _ in range(rotacion): #Ciclo, para rotar
        # Guarda el ultimo elemento
        ultimo_elemento = arreglo[-1]
        
        # Mueve cada elemento a su derecha
        for i in range(longitud-1, 0, -1):
            arreglo[i] = arreglo[i-1]
        
        # Mueve el ultimo elemento al principio
        arreglo[0] = ultimo_elemento
    return arreglo

arreglo = [1, 2, 3, 4, 5]
#Rotacion, define cuantas veces los elementos se moveran a su derecha
rotacion = 1  

#Se llama a la funcion y se le otorga el valor
resultado = rotar_elementos(arreglo, rotacion)
print(f"Arreglo rotado: {resultado}") #Salida
