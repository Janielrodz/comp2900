def area_triangulo(base, altura): #Funcion

    return (base * altura / 2) #Return, procedimiento

base = float(input("Ingrese la base del triangulo: ")) #Consulta al usuario
altura = float(input("Ingrese la altura del triangulo: ")) #Consulta al usuario

area = area_triangulo(base, altura) # se te otorga el resultado de la función a la variable

print(f"El area del triangulo es {area}") # Salida
