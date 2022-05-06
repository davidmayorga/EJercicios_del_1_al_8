"""Ejercicio; 1
Cordenadas cartesianas (p,y)"""



print("------------------------------------------------")
print("-----------Cuadrante plano cartesiano-----------")
print("------------------------------------------------")


#input
x=int(input("Digite coordenadas x: "))
y=int(input("Digite coordenadas y: "))


#processing
if x==0 and y==0:
    print("El punto esta sobre el eje x y el eje y")
elif x==0:
    print("El punto esta sobre el eje x")
elif y==0:
    print("l punto esta sobre el eje y:")

if x>0 and y<0:
    print("El punto pertenece al cuadrante I")
elif x<0 and y>0:
    print("El punto pertenece al cuadrate II")
elif x<0 and y<0:
    print("El punto pertenece al cuadrante III")
elif x>0 and y<0:
    print("El punto pertenece al cuadrante IV")
