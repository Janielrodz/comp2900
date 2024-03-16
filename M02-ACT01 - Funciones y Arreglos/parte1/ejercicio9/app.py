import random #Libreria de python
def generar_numeros_aleatorios(cantidad, minimo, maximo):
    #Se crea un arreglo vacío para los valores random
    numeros_aleatorios = []
    for _ in range(cantidad): #Ciclo
        #En la variable se almacena un numero aleatorio entre el minimo y maximo.
        numero = random.randint(minimo, maximo) 
        numeros_aleatorios.append(numero) #Se llena el arreglo
    return numeros_aleatorios

cantidad = int(input("Ingrese cuántos números desea generar: "))
minimo = int(input("Ingrese el número mínimo para generar el número aleatorio: "))
maximo = int(input("Ingrese el número máximo para generar el número aleatorio: "))

resultado = generar_numeros_aleatorios(cantidad, minimo, maximo) # Llama la función con los parámetros 
print(f"Números aleatorios generados: {resultado}")



    
