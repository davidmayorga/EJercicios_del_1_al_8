"""Ejercicio; 3
Dar precio del articulo"""



print("-------------------------------------------------")
print("----------------Precio del articulo----------------")
print("-------------------------------------------------")


#input
precio_costo=float(input("Dame el precio del costo del articulo: "))

#processing

if precio_costo<3000:
    ganancia=0.15*precio_costo
else:
    if precio_costo<=6000:
        ganancia=500
    else:
        ganancia=precio_costo*0.25

#output
p=precio_costo+ganancia

print("El precio de venta del articulo de costo: "+str(precio_costo)+ " es: "+str(p))