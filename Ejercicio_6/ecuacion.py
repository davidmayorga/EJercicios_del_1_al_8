"""Ejercicio 6:
Programa para calcular las posibles
 soluciones de una ecuacion de segundo grado."""

print("-------------------------------------------------")
print("----------ECUACIONES DE SEGUNDO GRADO------------")
print("-------------------------------------------------")

# input

print("ax^2+bx+c=0")
A=input("Digite el valor de A :")
A=int (A)
B=input("Digite el valor de B :")
B=int (B)
C=input("Digite el valor de C :")
C=int (C)

import math

# processing

D=B**2-(4*A*C)

if D<0:
    print("No hay soluciones son raices imaginarias")

elif D==0:
    X=-B/(2+A)
    print ("Tiene una unica solucion:"+ str (X))
    
elif D>0:

    X1=(-B+(D**0.5))/2*A
    X2=(-B-(D**0.5))/2*A
    print("Tiene dos soluciones X1 y X2" )
    print ("X1: "+ str (X1))
    print ("X2: "+ str (X2))