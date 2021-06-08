dia = int(input("Digita el día: "))
mes = int(input("Digita el mes: "))
año = int(input("Digita el año: "))

if año > 0:
    if mes > 0 and mes <= 12:
        maximo_dias = 31
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            maximo_dias = 30
        else:
            if mes == 2:
                if año % 4 == 0:
                    if año % 400 == 0:
                        #Es bisiesto
                        maximo_dias = 29
                    else:
                        if año % 100 == 0:
                            #No es bisiesto
                            maximo_dias = 28
                        else:
                            #Sí es bisiesto
                            maximo_dias = 29
                else:
                    #No es bisiesto
                    maximo_dias = 28
        
        #Validar el día
        if dia > 0 and dia <= maximo_dias:
            print("Fecha correcta")
        else:
            print("El día es incorrecto")
    else:
        print("El mes es incorrecto")
else:
    print("El año es incorrecto")