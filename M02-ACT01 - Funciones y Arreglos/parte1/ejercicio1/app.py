def maximo (a, b): #funcion
    
    if a > b: #condicion
        return a
    
    else: 
        return b
        
a = int(input("Ingrese el primer número: ")) #Consulta al usuario
b = int(input("Ingrese el segundo número: ")) #Consulta al usuario
    
resultado = maximo(a, b) #Se crea una variable para otorgarle el resultado de la funcion a la variable
print(f"El número máximo es {resultado}") #Imprime el resultado
 