
from Database.Conexion import Conexion
from Model.Hotel import Hotel
from Model.TipoHabitacion import TipoHabitacion
from Model.Habitacion import Habitacion


class HotelDAO:
    
    def __init__(self):
       self.conn = Conexion()
       
    def listarHoteles(self):
        try:
            conexion = self.conn.obtenerConexion()
            with conexion.cursor() as cursor:
                
                cursor.execute(""" 
                        SELECT 
                            h.id as hotel_id,
                            h.nombre AS hotel_nombre, 
                            h.direccion AS hotel_direccion, 
                            th.id AS tipo_id,
                            th.descripcion AS tipo_habitacion,
                            ha.id AS habitacion_id, 
                            ha.numero_habitacion, 
                            ha.precio
                        FROM hotel h
                        LEFT JOIN tipo_habitacion th ON h.Id = th.hotel_id
                        LEFT JOIN habitacion ha ON th.Id = ha.tipo_id;
                        """)
                
                listado = cursor.fetchall()
                
                hotelHabitaciones = {}  # Usamos un diccionario para evitar duplicados
                    
                for item in listado:
                    # Creamos el hotel si no existe en el diccionario
                    if item[0] not in hotelHabitaciones:
                        hotelHabitaciones[item[0]] = Hotel(item[0], item[1], item[2])
                    
                    hotel = hotelHabitaciones[item[0]]
                    # Creamos el tipo de habitación
                    tipoHabitacion = TipoHabitacion(item[3], item[4], hotel)
                    # Creamos la habitación y asociarla al hotel
                    habitacion = Habitacion(item[5], item[6], tipoHabitacion, item[7])
                    
                    hotel.habitaciones.append(habitacion)  # Añadir habitación directamente a la lista
                # Retornamos solo los valores del diccionario   
                return list(hotelHabitaciones.values()) 
                    
        except Exception as ex:
            print(f"Error al listar los hoteles: {ex}")
            return None
        finally:
            if conexion:
                conexion.close()
    
    def registrarHotel(self, nombre, direccion, descripcion_tipo, numero_habitacion, precio):
        try:
            conexion = self.conn.obtenerConexion()  
            with conexion.cursor() as cursor:
                # Insertamos el hotel
                query_hotel = """
                    INSERT INTO hotel (nombre, direccion)
                    VALUES (%s, %s)
                """
                values_hotel = (nombre, direccion)
                cursor.execute(query_hotel, values_hotel)
                hotel_id = cursor.lastrowid  # ID del hotel recién creado
                
                # Insertamos el tipo de habitación para el hotel
                query_tipo_habitacion = """
                    INSERT INTO tipo_habitacion (descripcion, hotel_id)
                    VALUES (%s, %s)
                """
                values_tipo_habitacion = (descripcion_tipo, hotel_id)
                cursor.execute(query_tipo_habitacion, values_tipo_habitacion)
                tipo_id = cursor.lastrowid  # ID del tipo de habitación recién creado
                
                # Insertamos la habitación asociada al tipo de habitación
                query_habitacion = """
                    INSERT INTO habitacion (numero_habitacion, tipo_id, precio)
                    VALUES (%s, %s, %s)
                """
                values_habitacion = (numero_habitacion, tipo_id, precio)
                cursor.execute(query_habitacion, values_habitacion)

            conexion.commit()
            print("Hotel registrado correctamente.")
        
        except Exception as ex:
            print(f"Error al registrar el hotel: {ex}")
            conexion.rollback()  # Deshacer los cambios en caso de error
        
        finally:
            if conexion:
                conexion.close()  # nos aseguramos de cerrar la conexión

    def buscarHoteles(self, hotel_nombre, hotel_direccion):
        try:
            conexion = self.conn.obtenerConexion()
            with conexion.cursor() as cursor:
                
                query = """ 
                        SELECT 
                            h.id as hotel_id,
                            h.nombre AS hotel_nombre, 
                            h.direccion AS hotel_direccion, 
                            th.id AS tipo_id,
                            th.descripcion AS tipo_habitacion,
                            ha.id AS habitacion_id, 
                            ha.numero_habitacion, 
                            ha.precio
                        FROM hotel h
                        LEFT JOIN tipo_habitacion th ON h.Id = th.hotel_id
                        LEFT JOIN habitacion ha ON th.Id = ha.tipo_id
                        WHERE h.nombre LIKE %s OR h.direccion LIKE %s
                        """
                
                # Uso de `%` para búsquedas parciales
                values = (f"%{hotel_nombre}%", f"%{hotel_direccion}%")
                cursor.execute(query, values)  
                hotel = cursor.fetchall()
                
                if hotel:
                    # Construir el hotel con sus habitaciones y tipos
                    hotel_dict = {}  # Para evitar duplicar hoteles
                    for item in hotel:
                        hotel_id = item[0]
                        if hotel_id not in hotel_dict:
                            # Creamos el objeto Hotel si no existe
                            hotel_dict[hotel_id] = Hotel(item[0], item[1], item[2])
                        
                        # Creamos el tipo de habitación y la habitación
                        tipo_habitacion = TipoHabitacion(item[3], item[4], hotel_dict[hotel_id])
                        habitacion = Habitacion(item[5], item[6], tipo_habitacion, item[7])
                        
                        # Asociamos la habitación al hotel
                        hotel_dict[hotel_id].habitaciones.append(habitacion)
                    
                    # Retornamos la lista de hoteles encontrados
                    return list(hotel_dict.values())
                else:
                    return None
        except Exception as ex:
            print(f"Error al buscar hoteles: {ex}")
            return None
        finally:
            if conexion:
                conexion.close()

    def listarHotelesHabitacion(self): # Metodo para la opcion 4 del menu
        try:
            conexion = self.conn.obtenerConexion()
            with conexion.cursor() as cursor:
                # Consulta para obtener los hoteles
                query = "SELECT id, nombre, direccion FROM hotel"
                cursor.execute(query)
                hoteles = cursor.fetchall()
                return hoteles
        except Exception as ex:
            print(f"Error al listar hoteles: {ex}")
            return []
        finally:
            if conexion:
                conexion.close()

   
    