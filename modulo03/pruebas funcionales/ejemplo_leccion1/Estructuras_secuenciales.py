def calcular_promedio(num1, num2):
    return (num1 + num2) /2
#Prueba
promedio_calculado = calcular_promedio(4, 6)

#El assert solo se usa en pruebas.
assert promedio_calculado != 5, "El promedio calculado es correcto." 