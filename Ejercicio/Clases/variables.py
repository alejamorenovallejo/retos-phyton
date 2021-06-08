#mi primera línea de código en Phyton
print("Hola Mundo")

#declaración variables
num1 = 5 * 8 + 3
num2 = 7 + 2 * 6.0
print(num1, type(num1))
print(num2, type(num2))
print(num1, num2)

#leer del teclado
num1= int(input("Escribe el primer número: "))
num2= int(input("Escribe el primer número: "))
sum=num1+num2
respuesta=print("La suma es " + str(sum))

#booleano
booleano= True
otro_booleano= False

#Fecha Correcta
dia=int(input("Favor digitar fecha día (DD)"))
if dia<1 or dia>31:
    print("Fecha dia no existe")
else:
    mes=int(input("Favor digitar fecha mes (MM)"))
    if mes<1 or mes>12:
        print("fecha mes no existe")
    else:
        ano=int(input("Favor digitar Fecha año (AAAA)"))
        if(mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
            print("De acuerdo al mes, el día no existe")
        else:
            if mes==2:
                if ano%4==0 and ano%100 != 0 and dia<=29:
                    print(dia,"-",mes,"-",ano," Año bisiesto")
                else:
                    print("De ")    

