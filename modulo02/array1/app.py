import array

aNumber = array.array('i')

for i in range(1, 4):
    number = int(input('Enter a number: '))
    aNumber.append(number)

for i in range(3): # from 0 to 4
    print(f'Indice {i} - {aNumber[i]}')

for n in aNumber:
    print(f'Valor {n}')

for i in range(len(aNumber)): #From 0 to 2
    print(f'Indice {i} - valor {aNumber[i]}')