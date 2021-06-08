#for loop(ciclo)
suma = 0 #Esto es un Acumulador
cuenta = 0 #Este es un contador
numero = int(input("¿Hasta que número quieres sumar?"))
for i in range(numero + 1):
    suma += i
    cuenta += 1
print("La suma de los números es ", suma)
print("El ciclo se ejecuto ", cuenta, "veces")


#Pero quiero que mi programa empiece desde 1 y no desde 0
suma2 = 0 #Esto es un Acumulador
cuenta2 = 0 #Este es un contador
for i in range(1,numero + 1):
    suma2 += i
    cuenta2 += 1
print("La suma de los números es ", suma2)
print("El ciclo se ejecuto ", cuenta2, "veces")

#Ahora quiero imprimir los pares
suma3 = 0 #Esto es un Acumulador
cuenta3 = 0 #Este es un contador
for i in range(2,numero + 1,2):
    suma3 += i
    cuenta3 += 1
print("La suma de los números pares ", suma3)
print("El ciclo se ejecuto ", cuenta3, "veces")