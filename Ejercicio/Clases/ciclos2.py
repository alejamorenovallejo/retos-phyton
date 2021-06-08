#Ahora vamos a sumar los pares pero filtrando con un if
#suma3 = 0 #Esto es un Acumulador
#cuenta3 = 0 #Este es un contador
#for i in range(2,numero + 1,2):
#    suma3 += i
#    cuenta3 += 1
#print("La suma de los números pares ", suma3)
#print("El ciclo se ejecuto ", cuenta3, "veces")

suma2=0
contador = 0 #Contador
for i in range(5):
    numero = int(input("Dame iun número que no sea cero"))
    if numero != 0 : 
        suma2=suma2+numero
        contador = contador + 1
    else:
        print("Te lo dije")
        break #Detiene el for más no el programa



print("Estoy probando contador vale",contador )
print("La suma  es ", suma2)
if contador>0:
    promedio = suma2 / contador
    print("El promedio es ", promedio)
else :
    print("no se puede calcular el promedio")

