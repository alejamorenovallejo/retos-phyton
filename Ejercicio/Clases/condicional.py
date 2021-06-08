num1 = float(input("Digita el primer número: "))
texto2 = input("Digita el segundo número: ")

num2 = float(texto2)

mayor = 0

if num1 > num2:
    mayor = num1
else:
    mayor = num2

print("El mayor es", mayor)

if mayor % 2 == 0:
    print("Y además es par")

if False:
    #Esto nunca ocurrirá
    print("Soy verdadero")
else:
    #Esto ocurrirá siempre
    print("Soy falso")