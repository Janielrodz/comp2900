def eliminar_elemento(arreglo, valor): #Funcion
    print(f"arreglo original: {arreglo}") #Muestra el arreglo original
    arreglo.remove(valor) #Borra 1 valor de la lista
    return arreglo

arreglo = [2004, 2002, 2000, 1998, 1996] 
valor_a_eliminar = 1998  # Valor que se va a eliminar.

resultado = eliminar_elemento(arreglo, valor_a_eliminar)
print(f"Arreglo después de eliminar el elemento: {resultado}")



