payRate = float(input("Pago por Hora: "))
hourRate = float(input("Horas Trabajadas: "))

overtimeHours = 0

if (hourRate > 40):
    overtimeHours = hourRate - 40
    totalPayment = (40 * payRate) + (overtimeHours * (payRate * 2))



else:
    totalPayment = (payRate * hourRate)

print(f"Your total payment is {totalPayment} ")
    