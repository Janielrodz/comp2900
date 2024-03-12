def temperatura(fahrenheit): #funcion
    return ((fahrenheit - 32) * 5/9) #el valor que devuelve la función

fahrenheit = float(input("Ingrese la temperatura en grados fahrenheit: ")) #Consulta al usuario

celsius = temperatura(fahrenheit) #La variable celsius adquiere lo que devuelve la funcion
print(f"La temperatura en grados celsius es {celsius} grados.") #Salida del programa



