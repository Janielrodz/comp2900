def arreglos_combinados():
    print(f"Arreglo 1: {arreglo1}")
    print(f"Arreglo 2: {arreglo2}")

    #Procedimiento, la suma de ambos arreglos.
    arreglo_final = arreglo1 + arreglo2
    return arreglo_final #Devuelve el resultado de los arreglos.

#Se definen los arreglos.
arreglo1 = [1, 2, 3, 4, 5]
arreglo2 = [6, 7, 8, 9, 10]

#Se llama la función
resultado = arreglos_combinados()
print(f"La combinación de ambos arreglos es: {resultado}") #Salida