"""Ejercicio 9:
Programa que por cada número ingresado del 1 al 7 
diga que dia de la semana es en ese orden"""


print("------------------------------------")
print("---------DIAS DE LA SEMANA----------")
print("------------------------------------")


# input
OP=int(input("Digite un número del 1 al 7: "))


#processing
if OP==1:
  print("Es Lunes")
elif OP==2:
  print("Es Martes")
elif OP==3:
  print("Es Miércoles")
elif OP==4:
  print("Es Jueves")
elif OP==5:
  print("Es Viernes")
elif OP==6:
  print("Es Sábado")
elif OP==7:
  print("Es Domingo")
else:
  print("Día no válido")