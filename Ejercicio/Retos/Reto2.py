respuesta = "s"
while respuesta == "s" or respuesta == "S" or respuesta == "si" or respuesta == "SI":
    #Declaracion de Variables
    cotizacion=[]
    suma = 0
    #Solicitud NIT,Nombre y Valor 
    for indice in range(5):
        nit = input("Ingrese el NIT: ")
        while nit == '':
            nit = input("Ingrese el NIT: ")
        nombre = input("Ingrese el Nombre: ")
        while nombre=='':
            nombre = input("Ingrese el Nombre: ")
        valor=int(input("Ingrese el Valor: "))
        try:
            while (valor == 0) :
                valor = input("Escribe un Valor: ")
        except:
            print ("Se deben ingresar valores númericos")
            valor = int(input("Escribe un Valor: "))
        
        #Creación del arreglo
        cotizacion.append([nit,nombre,valor])
    
    # Se Inicializa y se asume que tanto el mayor valor de cotizacion como el menor valor de cotización están en el primer elemento; 
    mayor = cotizacion[0][2]
    menor = cotizacion[0][2]
    
    # Se recorre la matriz para obtener el valor mayor y menor de la cotización
    for fila in cotizacion:
        suma = suma + fila[2]
        valor=fila[2]
        if(valor >= mayor) :
            mayor = valor
            cotizacion_mayor = cotizacion.index(fila)    
        if(valor <= menor) :
            menor = valor
            cotizacion_menor = cotizacion.index(fila)  

    # promedio de las cotizaciones        
    promedio = suma / len(cotizacion)

    # Imprimir resultado de la cotización mas baja y la más alta y el promedio
    print("Cotización más baja")
    print("Nit: ",cotizacion[cotizacion_menor][0])
    print("Nombre: ",cotizacion[cotizacion_menor][1])
    print("Valor: ",cotizacion[cotizacion_menor][2])
    print("Cotización más alta")
    print("Nit: ",cotizacion[cotizacion_mayor][0])
    print("Nombre: ",cotizacion[cotizacion_mayor][1])
    print("Valor: ",cotizacion[cotizacion_mayor][2])
    print("Promedio: ", promedio)

    # se pregunta nuevamente si desea ingresar otra cotización
    respuesta = input("\n¿Desea realizar más cotizaciones? (si/no) ")






