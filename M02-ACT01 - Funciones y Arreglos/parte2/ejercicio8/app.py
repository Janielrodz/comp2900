def ordenar_arreglo(): 
    print(f"Arreglo original: {arreglo}") #Imprime el arreglo original

    arreglo.sort() #Ordena el arreglo
    return arreglo

arreglo = [89, 26, 30, 47, 51]

resultado = ordenar_arreglo() #Se inicializa

print(f"Arreglo modificado: {resultado}") #Salida


