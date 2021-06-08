from datetime import datetime

lista_pacientes=[]
lista_pacientes_superior =[]
respuesta = "s"
count = 0
while respuesta == "s" or respuesta == "S" or respuesta == "si" or respuesta == "SI":

    solicitud=True
    while solicitud:
        try:
            fecha_solicitud = datetime.strptime(input("Ingrese la Fecha de Solicitud (dd/mm/yyyy): "),'%d/%m/%Y')
            solicitud=False
        except ValueError:
            print("Fecha inválida")

    solicitud=True
    while solicitud:
        try:
            fecha_cita = datetime.strptime(input("Ingrese la Fecha de la Cita (dd/mm/yyyy): "),'%d/%m/%Y')
            if (fecha_cita > fecha_solicitud ):
                solicitud=False
        except ValueError:
            print("Fecha inválida")
        
    solicitud=True
    while solicitud:
        try:
            fecha_entrega_muestras = datetime.strptime(input("Ingrese la Fecha de entrega de muestras (dd/mm/yyyy): "), '%d/%m/%Y')
            if (fecha_entrega_muestras > fecha_cita):
                solicitud=False
        except ValueError:
            print("Fecha inválida")        

    solicitud=True
    while solicitud:
        nombres_paciente = input("Ingrese los Nombres del Paciente: ")
        if nombres_paciente !='':
            solicitud=False

    solicitud=True
    while solicitud:
        apellidos_paciente = input("Ingrese los Apellidos del Paciente: ")
        if apellidos_paciente !='':
            solicitud=False
    
    solicitud=True
    while solicitud:
        try:
            documento_paciente = int(input("Ingrese el número de documento del Paciente: "))
            if documento_paciente !=0:
                solicitud=False
        except:
            print ("Se deben ingresar valores númericos")

    solicitud=True
    while solicitud:
        try:
            telefono_paciente = int(input("Ingrese el número de teléfono del Paciente: "))
            if telefono_paciente !=0:
                solicitud=False
        except:
            print ("Se deben ingresar valores númericos")

    #Creación del arreglo de pacientes
    lista_pacientes.append([fecha_solicitud,fecha_cita,fecha_entrega_muestras,nombres_paciente,apellidos_paciente,documento_paciente,telefono_paciente])
    
    # se pregunta nuevamente si desea ingresar otra cotización
    respuesta = input("\n¿Desea ingresar más pacientes? (si/no) ")

#Recorrido de la lista de pacientes
for paciente in lista_pacientes:
    dias_entre_solicitud_cita = (paciente[1]-paciente[0])
    dias_entre_cita_muestras =(paciente[2]-paciente[1])
    nombres_apellidos_paciente = paciente[3] + " " +paciente[4]
    #Solicitud y Cita 2 dias siguientes maximo y Cita y entrega resultados 3 días maximo
    if (dias_entre_solicitud_cita.days > 2 or dias_entre_cita_muestras.days > 3) :
        count = count +1
        lista_pacientes_superior.append([count,dias_entre_solicitud_cita.days,dias_entre_cita_muestras.days,nombres_apellidos_paciente,paciente[6]])

# Imprimir resultado de la lista de pacientes con espera superior y el total de pacientes con espera superior
print("PACIENTES CON TIEMPOS DE ESPERA SUPERIORES A LO ESTABLECIDO")
for paciente_superior in lista_pacientes_superior:
    print(paciente_superior[0],")",paciente_superior[3], "-",paciente_superior[1],"días entre llamada y cita,",paciente_superior[2],"días entre cita y resultados – Teléfono:", paciente_superior[4])

print("Total de pacientes con tiempos superiores: ",len(lista_pacientes_superior))
