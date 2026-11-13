camarotes_disponibles = 90
opcion = 0
camarotes_reservados = 0
camarotes_elegidos = 0
cancelar_camarotes = 0
total_reservas= 0
reservas = 0
cancelacion = 0
print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")
while opcion != 5:
    print("1. Camarotes Disponibles")
    print("2. Reservar Camarote")
    print("3. Cancelar Camarote")
    print("4. Historial De Reservas")
    print("5. Salir Del Sistema")

    opcion = int(input("Elige una opcion del menu: "))

    match opcion:
        case 1:
            print("Quedan", camarotes_disponibles, " camarotes disponibles para reservar")
        case 2:
            camarotes_elegidos = int(input("Eliga cuantos camarotes quiere reservar: "))
            if camarotes_elegidos <= camarotes_disponibles and camarotes_elegidos > 0:
                camarotes_reservados = camarotes_reservados + camarotes_elegidos
                camarotes_disponibles = camarotes_disponibles - camarotes_elegidos
                reservas = reservas + 1
                print("camarote reservado con exito")
            elif camarotes_elegidos > camarotes_disponibles:
                print("no se pueden elegir mas camarotes de los disponibles")
            elif camarotes_elegidos <= 0:
                print("no se pueden elegir numeros negativos ni tampoco ceros")
        case 3:
            cancelar_camarotes = int(input("ingresa la cantidad de camarotes que quieres cancelar: "))
            if cancelar_camarotes <= camarotes_reservados and cancelar_camarotes > 0:
                camarotes_disponibles = camarotes_disponibles + cancelar_camarotes
                camarotes_reservados = camarotes_reservados - cancelar_camarotes
                cancelacion = cancelacion + 1
                print ("camarote cancelado con exito")
            elif cancelar_camarotes > camarotes_reservados:
                print("no se pueden elegir mas camarotes de los disponibles")
            elif cancelar_camarotes <= 0:
                print("no se pueden elegir numeros negativos ni tampoco ceros")
            else:
                print("no hay camarotes disponibles para cancelar")
        case 4:
            total_reservas = reservas - cancelacion
            print ("La cantidad total de reservas es de", total_reservas, "realizada durante el dia")
        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")