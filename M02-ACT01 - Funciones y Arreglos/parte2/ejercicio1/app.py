def sumar_elementos():
    arreglo = [6, 4]  # Arreglo de 2 valores numéricos.
    print(f"Arreglo: {arreglo}")
    suma = 0  #Se inicializa la variable suma a 0.
    for elemento in arreglo:  # Ciclo.
        suma += elemento  # Se crea un acumulador
    return suma

resultado = sumar_elementos()  # Se inicializa la funcion.
print(f"La suma de los elementos del arreglo es {resultado}") #Salida.
