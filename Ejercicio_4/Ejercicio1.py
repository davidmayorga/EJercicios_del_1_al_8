"""Ejercicio: 4
Programa pra calcular el indice de la mas corporal de una persona"""


from socket import IPPROTO_MPTCP


print("----------------------------------------------------------------")
print("------------------Programa para calcular el IMC-----------------")
print("----------------y indica el estado de la persona----------------")
print("----------------------------------------------------------------")


#input
peso=float(input("Digite su peso en kilogramos: "))
altura=float(input("Digite su altura en metros: "))


#processing and output

IMC=(peso/(altura*altura))

if IMC<16:
    print("ESta muy por debajo del peso apropiado\ncritico de ingreso al hospital")
else:
    if IMC<17:
        print("usted esta algo por debajo de su peso apropiado\ntiene infrapeso")
    else:
        if IMC<18:
            print("usted esta un poco por debajo de su peso apropiado \nUsted esta con bajo peso")
        else:
            if IMC<25:
                    print("Usted posee un peso apropiado \nes una persona saludable")
            else:
                if IMC<30:
                        print("Usted tiene sobre peso \n sobrepeso nivel I")
                else:
                    if IMC<35:
                        print("Usted sufre de bastante obecidad \n Tiene sobre peso cronico (obecidad nivel II)")
                    else:
                        if IMC<40:
                            print("Usted sufre de mucha obecidad \n posee obecidad premorvida (obecidad grado III)")    
                        else:
                            if IMC>40:
                                print("Usted sufre demaciada obecidad \n posee obecidad morvida (Obecidad grado IV)")
print(" Su imc es de "+ str(IMC))
