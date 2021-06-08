from datetime import datetime

# Solicitud de Datos Nombres,Apellidos,Dirección,Telefono,Sexo,Fecha de Nacimiento y Fecha de Procedimiento
nombres = input("Ingrese sus Nombres: ")
while (nombres) == '':
    nombres = input("Ingrese sus Nombres: ")

apellidos = input("Ingrese sus Apellidos: ")
while (apellidos) == '':
    apellidos = input("Ingrese sus Apellidos: ")

direccion = input("Ingrese su Dirección de Residencia: ")
while (direccion) == '':
    direccion = input("Ingrese su Dirección de Residencia: ")
try:
    telefono = int(input("Escribe un Teléfono: "))
    while (telefono) == 0:
        telefono = input("Escribe un Teléfono: ")
except:
    print ("Se deben ingresar valores númericos")
    telefono = int(input("Escribe un Teléfono: "))
    while (telefono) == 0:
            telefono = input("Escribe un Teléfono: ")

sexo = input("Ingrese su Sexo: ")
while (sexo) == '':
    sexo = input("Ingrese su Sexo: (F/M)")

if (sexo != 'F' or sexo != 'M'):
    sexo = input("Ingrese su Sexo: (F/M)")

fecha_nacimiento = input("Ingrese la Fecha de Nacimiento: ")
while (fecha_nacimiento) == '':
    fecha_nacimiento = input("Ingrese la Fecha de Nacimiento: ")

fecha_procedimiento = input("Ingrese la Fecha de realización del procedimiento: ")
while (fecha_nacimiento) == '':
    fecha_procedimiento = input("Ingrese la Fecha de realización del procedimiento: ")

#Formato de Fecha
fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
fecha_procedimiento = datetime.strptime(fecha_procedimiento, '%d/%m/%Y')

#Cálculo de Edad
edad = fecha_procedimiento.year - fecha_nacimiento.year
edad -= ((fecha_procedimiento.month,fecha_procedimiento.day) < (fecha_nacimiento.month,fecha_nacimiento.day))

#Sexo
if sexo=='F':
    sexo="Femenino"
else:
    if sexo=='M':
        sexo="Masculino"
    else:
        sexo="No Definido"

#Validación Ciclo Vital
if edad >=60:
    ciclovital="Persona mayor"
elif edad >=27 and edad <=59:
    ciclovital="Adultez"
elif edad >=19 and edad <=26:
	ciclovital="Juventud"
elif edad >=12 and edad <=18:
    ciclovital="Adolescencia"
elif edad >=6 and edad <=11:
	ciclovital="Infancia"
elif edad >=0 and edad <=5:
    ciclovital="Primera infancia"

#Validación de Segumiento
if edad<=55 and edad % 5 == 0:
    segumiento="Es necesario seguimiento detallado por edad"
else: 
    segumiento="No es necesario seguimiento detallado por edad"

#Mostar Ficha
print("Nombre: ", nombres,apellidos)
print("Dirección de residencia: ",direccion)
print("Teléfono: ", telefono)
print("Sexo: ",sexo)
print("Edad: ",edad)
print("Ciclo vital: ",ciclovital)
print(segumiento)





