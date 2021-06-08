num1 = int(input("Digita el primer número: "))
num2 = int(input("Digita el segundo número: "))

#Suma
suma = num1 + num2
print("La suma de", num1, "y", num2, "es igual a", suma)

#Sumar un valor a una variable y guardar en la misma variable
#Primera forma
suma = suma + 5
print("Al resultado le sumo 5 y obtengo", suma)
#Segunda forma
suma += 5
print("Vuelvo a sumar 5 y obtengo", suma)

#Resta
resta = num1 - num2
print("La resta de", num1, "y", num2, "es igual a", resta)

#Restar un valor a una variable y guardar en la misma variable
#Primera forma
resta = resta - 5
print("Al resultado le resto 5 y obtengo", resta)
#Segunda forma
resta -= 5
print("Vuelvo a restar 5 y obtengo", resta)

#Multiplicación
multiplicacion = num1 * num2
print("Multiplicación", multiplicacion)
multiplicacion *= 5
print("Multiplicación por 5", multiplicacion)

#Divisón
division = num1 / num2
print("División", division)
division /= 5
print("División por 5", division)

#Potencia
potencia = num1**num2
print("Potencia", potencia)
potencia **= 2
print("Elevar a la 2", potencia)

#División entera
division_entera = num1 // num2
print("División entera", division_entera)
division_entera //= 5
print("División por 5", division_entera)

#Residuo o módulo
residuo = num1 % num2
print("Residuo", residuo)
residuo %= 5
print("Residuo al dividir entre 5", residuo)