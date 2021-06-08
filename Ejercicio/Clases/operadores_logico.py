#Valores booleanos
bol1 = True
print(bol1, type(bol1))
bol2 = False
print(bol2, type(bol2))

texto1 = input("Digita el primer texto: ")
texto2 = input("Digita el segundo texto: ")

#Igualdad
bol3 = texto1 == texto2
print("igualdad", bol3)

#Diferencia
bol3 = texto1 != texto2
print("Diferentes", bol3)

#Mayor que
bol3 = texto1 > texto2
print("Mayor que", bol3)

#Menor que
bol3 = texto1 < texto2
print("Menor que", bol3)

#Mayor o igual
bol3 = texto1 >= texto2
print("Mayor o igual", bol3)

#Menor o igual
bol3 = texto1 <= texto2
print("Menor o igual", bol3)

print("¿Eres joven?")
edad = int(input("Dime tu edad: "))
joven = edad >= 19 and edad <= 26
print("Respuesta:", joven)

#Existen dos operadores de comáración lógica, el and y el or

#Existe un operador de negación
bol4 = False
print("Valor inicial", bol4)
bol4 = not bol4
print("Valor negado", bol4)