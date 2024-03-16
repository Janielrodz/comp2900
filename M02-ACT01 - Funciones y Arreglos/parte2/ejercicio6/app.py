def contar_apariciones():
    print(f"Arreglo: {arreglo}")
    suma = 0 #Se inicializa la variable con 0.

    #Se crea un ciclo para el elemento escogido del arreglo.
    for elemento_seleccionado in arreglo: 
        if elemento_seleccionado == 45: #Condicion
            suma += 1 #Acumulador, va sumando de 1 en 1.
    return suma

arreglo = [45, 50, 45, 60, 45, 80]  
resultado = contar_apariciones() #Se inicializa la funcion.
print(f"El numero 45 se repite {resultado} veces.")

