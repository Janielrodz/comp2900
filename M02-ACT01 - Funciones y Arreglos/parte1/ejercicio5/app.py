def encontrar_indice(lista, elemento): #Funcion
    if elemento in lista: #Condición, si el elemento está en la lista mostrará el número índice.
        return lista.index(elemento) #Devuelve el indice
    
    else: # De lo contrario mostrará -1.
        return -1

lista = [5, 6, 7, 8, 9, 10] #Lista de numeros
elemento = 8 #Elemento indice

numero_encontrad0 = encontrar_indice(lista, elemento)

print(f"El indice de la lista es: {numero_encontrad0}") #Salida
