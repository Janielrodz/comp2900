def maximo(arreglo, n): #Funcion
    largo = arreglo[0] #Se crea la variable largo y el primer elemento del arreglo.
    for i in range(1, n): #Se crea un ciclo que comienza en 1 y llega hasta las veces que el usuario decida.
        if largo < arreglo[i]: #Condición
            largo = arreglo[i]
    return largo

arreglo = [] #Se crea un arreglo, para que el usuario lo llene.
n = int(input("Ingrese de cuantos elementos desea su arreglo: ")) #Se le consulta al usuario el tamaño del arreglo.

for i in range(0, n): #Se crea un ciclo desde 0 hasta n, que sería el numero ingresado por el usuario.
    elemento = int(input("Ingrese los elementos: ")) #Se le pide al usuario los elemntos.
    arreglo.append(elemento) #Se usa el metodo append, determina el elemento mas grande de un arreglo.

print(arreglo) #Imprime el arreglo creado por el usuario.
resultado = maximo(arreglo, n) #Se le otorga lo que devuelve la función a la variable.
print(f"El elemento más grande del arreglo es: {resultado}") #Salida
    