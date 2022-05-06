"""Ejercicio: 
Prestamo"""



print("-------------------------------------------------")
print("----------------Valor de ingresos----------------")
print("-------------------------------------------------")


#input
Ingresos=int(input("Ingrese el numero de sus ingresos "))

#processing
if Ingresos>945200:
    deudas=int(input(" ponga 0 si no tiene deudas o ponga 1 si tiene deudas "))
    if deudas==0:
        print(" aprobado el prestamo ")
    else:
     print(" no puede ser aprobado ")
else:
    print(" no puede ser aprobado ")
