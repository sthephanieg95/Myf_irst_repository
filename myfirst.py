horas=float(input("Introduzca las horas:  \n"))
tarifa=float(input("introduzca la tarifa por hora:  \n"))
if horas > 40:
    r1=tarifa*horas
    r2=(horas-40)*(tarifa*0.5)
    rf=r1+r2
else:
    rf=tarifa*horas
print("resultado: " + str(rf))
