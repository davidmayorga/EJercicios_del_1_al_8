"""Ejercicio 8:
Programa que lea dos números enteros
y averigüe si el uno es múltiplo del otro"""


print("-------------------------------")
print("------------MULTIPLOS----------")
print("-------------------------------")


# input
A=int(input("Digite el valor del primer numero: "))
B=int(input("Digite el valor del segundo numero: "))


#processing
if A>B:
    X=A/B
    if (int(X)==X):
      print("El numero "+str(A)+" es múltiplo del número "+str(B))
    else:
      print("El numero "+str(A)+" NO es múltiplo del número "+str(B))
else:
    X=B/A
    if (int(X)==X):
        print("El numero "+str(B)+" es múltiplo del número "+str(A))
    else:
     print("El numero "+str(B)+" NO es múltiplo del número "+str(A))

#Fin
