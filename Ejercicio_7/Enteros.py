"""Ejercicio 7:
Programa para determinar si dados tres números enteros,
la suma de los dos primeros es igual al tercero"""


print("----------------------------------")
print("-------SUMA DE DOS ENTEROS -------")
print("----------------------------------")


# input
X=int(input("Digite el valor del primer entero: "))
Y=int(input("Digite el valor del segundo entero: "))
C=int(input("Digite el valor del tercer entero: "))


#processing

Z=X+Y
if Z==C:
    print("La suma de los dos primeros enteros es igual al tercero")
else:
    print("La suma de los dos primeros no es igual al tercer entero")