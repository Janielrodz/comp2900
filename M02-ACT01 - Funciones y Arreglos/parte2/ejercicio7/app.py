def promedio(lista_numeros):
    suma = 0 # Se inicializa la variable suma a 0.
    for numero in lista_numeros: #Ciclo
        suma += numero
        #Devuelve la suma de todos los elementos del arreglo sobre el largo del arreglo
    return suma / len(lista_numeros) 

lista_numeros = [10, 20, 30, 40, 50] 
resultado = promedio(lista_numeros) #Se inicializa la función
print(f"El promedio de la lista es de {resultado}") #Salida