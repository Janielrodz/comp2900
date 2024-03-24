lista = [10, 3, 4, 7, 5]

print(4 in lista) #O(n)

suma = 0
for number in lista: #O(n)
    suma += number

for i in range(len(lista)- 1): #0(n^2)
    for j in range(len(lista)- i -1):
        if lista[j] >