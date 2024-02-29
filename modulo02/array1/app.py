import array

aNumber = [0] * 3

for i in range(1, 4):
    number = int(input('Enter a number: '))
    aNumber[i-1] = number
    #

for i in range(3): # from 0 to 4
    print(f'Indice {i} - Valor {aNumber[i]}')

aNumber.sort()

for n in aNumber:
    print(f'Valor {n}')

for i in range(len(aNumber)): #From 0 to 2
    print(f'Indice {i} - valor {aNumber[i]}')