from Controller.HotelDAO import HotelDAO
from Controller.TipoHabitacionDAO import TipoHabitacionDAO
from Controller.HabitacionDAO import HabitacionDAO

import os
os.system('clear')

def iniciarAplicacion():
    opcion = 0
    daoHotel = HotelDAO()
    daoTipoHabitacion = TipoHabitacionDAO()
    daoHabitacion = HabitacionDAO()
    

    while opcion !=7:
        try:
            print("=" * 30)
            print("       MENU PRINCIPAL")
            print("=" * 30)
            print("1.- Hoteles y habitaciones Disponibles")
            print("2.- Registrar Hotel")
            print("3.- Buscar Hotel")
            print("4.- Agregar Habitación a hotel")
            print("5.- Eliminar Habitación de hotel")
            print("6.- Mostar precios en dolares")
            print("7.- Salir")
            print("" * 30)

            opcion = int(input("Seleccione una opción: "))

            if opcion in (1,2,3,4,5,6,7):
                if opcion == 1:
                    print("")
                    print("Hoteles y habitaciones Disponibles")
                    print("=" * 40)
                    print("")
                    hoteles = daoHotel.listarHoteles()  # Asigna el resultado de la consulta a hoteles
                    if hoteles:
                        for hotel in hoteles:
                            hotel.mostrarDatos()  # Mostrará tanto los datos del hotel como sus habitaciones
                            print("")
                    else:
                        print("No hay hoteles disponibles.")
                    print("")
                    print("=" * 40)
                
                if opcion == 2:
                    print("\nRegistrar Hotel")
                    print("=" * 40)
                    print("")
                    
                    # Solicitamos datos del hotel
                    nombre = input("Ingrese el nombre del hotel: ")
                    direccion = input("Ingrese la dirección del hotel: ")

                    # Mostramos tipos de habitación disponibles
                    tipos = daoTipoHabitacion.obtenerTiposHabitacion()
                    print("\nSelecciona un tipo de habitación:")
                    print("")
                    for tipo in tipos:
                        print(tipo.menuTiposHabitacion())
                    print("")
                    tipo_id = (input("\nIngrese el tipo de habitación: (Ejemplo: Doble)")) # Ingresamos el tipo de habitacion
                    try:
                        numero_habitacion = input("Ingrese el número de la habitación (Ejemplo: S403): ") # Solicitamos el número de la habitación
                        precio = float(input("Ingrese el precio de la habitación en Pesos (Ejemplo: 85000): ")) #Solicitamos el precio de la habitación

                        # Registramos el hotel y la habitación asociada
                        daoHotel.registrarHotel(nombre, direccion, tipo_id, numero_habitacion, precio)
                    
                    except ValueError:
                        print("Error: El ID del tipo de habitación y el precio deben ser numéricos.")
                    except Exception as ex:
                        print(f"Error al registrar el hotel: {ex}")
                    
                elif opcion == 3:
                    print("\nBuscar Hotel por nombre o dirección\n")
                    print("=" * 40)
                    try:
                        # Solicitamos el nombre o dirección del hotel
                        nombrehotel = input("Ingresa el nombre o la dirección del hotel a buscar: ").strip()
                        
                        if nombrehotel:  # Verificamos que se ingresó algo
                            hoteles = daoHotel.buscarHoteles(nombrehotel, nombrehotel)  # Buscar hoteles
                            if hoteles:
                                print("\nResultados de la búsqueda:\n")
                                for hotel in hoteles:
                                    hotel.mostrarDatos()  # Mostrar los datos de cada hotel encontrado
                            else:
                                print("\nNo se encontraron hoteles con el nombre o dirección ingresados.")
                        else:
                            print("\nDebes ingresar un nombre o dirección para realizar la búsqueda.")
                    except Exception as ex:
                        print(f"\nError al buscar hotel: {ex}")

                elif opcion == 4:
                    print("\nAgregar habitación a hotel:")
                    print("=" * 40)

                    # Listar los hoteles
                    hoteles = daoHotel.listarHotelesHabitacion()
                    if not hoteles:
                        print("No hay hoteles disponibles. Regresa más tarde.")
                    else:
                        while True:  # Validar el ID del hotel
                            print("\nSelecciona un hotel:")
                            for hotel in hoteles:
                                print(f"ID: {hotel[0]} - Nombre: {hotel[1]} - Dirección: {hotel[2]}")
                            try:
                                hotel_id = int(input("\nIngrese el ID del hotel al que desea agregar la habitación: "))
                                if any(hotel[0] == hotel_id for hotel in hoteles): # Verificamos que el ID ingresado esté en la lista de hoteles
                                    break
                                else:
                                    print("El ID del hotel ingresado no es válido. Intenta nuevamente.")
                            except ValueError:
                                print("Por favor, ingrese un número válido.")

                        # Opciones fijas de tipos de habitación - esto lo hice porque si hacia la consulta directo a la tabla me traia todos los id y no solo los 3 tipos de habitaciones aunque usara distinct o group by 
                        tipos_fijos = ["Individual", "Doble", "Suite"]
                        while True: #inicio ciclo
                            print("\nSelecciona un tipo de habitación:")
                            for i, tipo in enumerate(tipos_fijos, 1): # Enumeramos las opciones en la lista `tipos_fijos` comenzando desde 1
                                print(f"{i}. {tipo}")
                            try:
                                opcion_tipo = int(input("\nIngrese el número del tipo de habitación: ")) # Verificamos que el número ingresado esté dentro del rango válido
                                if 1 <= opcion_tipo <= len(tipos_fijos):
                                    descripcion_tipo = tipos_fijos[opcion_tipo - 1] # Obtiene la descripción del tipo seleccionado
                                    break # Si la entrada es válida, rompe el ciclo y continúa con el flujo
                                else:
                                    print("Opción no válida. Intenta nuevamente.")
                            except ValueError:
                                print("Por favor, ingrese un número válido.")

                        # Solicitamos los datos de la nueva habitación
                        while True:  # Validamos que el número de habitación no esté vacío
                            numero_habitacion = input(" Ingrese un número de habitación (Ejemplo: S403): ").strip()
                            if numero_habitacion:
                                break
                            else:
                                print("El número de habitación no puede estar vacío.")

                        while True:  # Validamos que el precio sea un número válido
                            try:
                                precio = float(input(" Ingrese el precio en pesos (Ejemplo: 80000): "))
                                break
                            except ValueError:
                                print("Por favor, ingrese un precio válido.")

                        # Registramos la habitación
                        daoHabitacion.agregarHabitacion(numero_habitacion, descripcion_tipo, precio, hotel_id)

                elif opcion == 5:  # Opción para eliminar una habitación
                    print("\nEliminar habitación de un hotel:")
                    print("=" * 40)
                    # Listamos los hoteles -  otro de los tantos metodos para listar hoteles, en este caso solo se listan los hoteles que tienen habitaciones
                    hoteles = daoHotel.listarHotelesHabitacion()
                    if not hoteles:
                        print("No hay hoteles disponibles.")
                    else:
                        while True:  # Validamos el ID del hotel
                            print("\nSelecciona un hotel:")
                            for hotel in hoteles:
                                print(f"ID: {hotel[0]} - Nombre: {hotel[1]} - Dirección: {hotel[2]}")
                            try:
                                hotel_id = int(input("\nIngrese el ID del hotel: "))
                                if any(hotel[0] == hotel_id for hotel in hoteles): # Verificamos que el ID ingresado esté en la lista de hoteles
                                    break
                                else:
                                    print("El ID ingresado no es válido.")
                            except ValueError:
                                print("Por favor, ingrese un número válido.")

                        # Listamos las habitaciones del hotel seleccionado
                        habitaciones = daoHabitacion.listarHabitacionesPorHotel(hotel_id)
                        if not habitaciones:
                            print(f"El hotel con ID {hotel_id} no tiene habitaciones registradas.")
                        else:
                            while True:
                                print("\nHabitaciones disponibles:")
                                for habitacion in habitaciones:
                                    print(f"ID: {habitacion[0]}, Número: {habitacion[1]}, Tipo: {habitacion[2]}, Precio: {habitacion[3]}") 
                                try:
                                    habitacion_id = int(input("\nIngrese el ID de la habitación a eliminar: "))
                                    if any(h[0] == habitacion_id for h in habitaciones):   # Verificamos que el ID ingresado esté en la lista de habitaciones
                                        daoHabitacion.eliminarHabitacion(habitacion_id)  # Eliminar la habitación
                                        break
                                    else:
                                        print("El ID de la habitación ingresado no es válido.")
                                except ValueError:
                                    print("Por favor, ingrese un número válido.")

                elif opcion == 6:  #opción para mostrar precios en dólares
                    print("")
                    print("Hoteles y habitaciones Disponibles (Precios en USD)")
                    print("=" * 40)
                    print("")
                    hoteles = daoHotel.listarHoteles()  # Asigna el resultado de la consulta a hoteles
                    if hoteles:
                        for hotel in hoteles:
                            hotel.mostrarDatosDolares()  # Mostrará tanto los datos del hotel como sus habitaciones en dolares
                            print("")
                    else:
                        print("No hay hoteles disponibles.")
                    print("")
                elif opcion == 7 :
                    print("")
                    print("Saliendo de la aplicación")
                    break
            else:
                print("Opción no válida")

        except ValueError:
            input("Debe ingresar solo números, presione una tecla para continuar")
