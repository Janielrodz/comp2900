def encontrar_elemento(): #Funcion
    #Se crea una variable local que almacena el indice que determine el usuario.
    elemento_encontrado = arreglo.index(elemento_ingresado)
    return elemento_encontrado #Devuelve el elemento encontrado

arreglo = [10, 20, 30, 40, 50]
print(f"Arreglo completo: {arreglo}")
elemento_ingresado = int(input("Ingrese el elemento del arreglo que desea corrobar: "))
resultado = encontrar_elemento()
print(f"La posición del elemento es: {resultado}")