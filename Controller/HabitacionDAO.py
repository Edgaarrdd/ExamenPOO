 
from Database.Conexion import Conexion
from Model import Habitacion
from Model.Hotel import Hotel
from Model.TipoHabitacion import TipoHabitacion

 
class HabitacionDAO():
    
    def __init__(self):
       self.conn = Conexion()
       
    def agregarHabitacion(self, numero_habitacion, descripcion_tipo, precio, hotel_id):
        try:
            conexion = self.conn.obtenerConexion()
            with conexion.cursor() as cursor:
                # Verificar si el número de habitación ya existe para el hotel
                query_verificacion_numero = """
                    SELECT COUNT(*) 
                    FROM habitacion h
                    JOIN tipo_habitacion th ON h.tipo_id = th.id
                    WHERE h.numero_habitacion = %s AND th.hotel_id = %s
                """
                cursor.execute(query_verificacion_numero, (numero_habitacion, hotel_id))
                if cursor.fetchone()[0] > 0: #comprobamos si el conteo es mayor a 0
                    print(f"El número de habitación '{numero_habitacion}' ya está registrado en este hotel.")
                    return

                # Verificamos si el tipo de habitación ya existe para el hotel
                query_verificacion_tipo = """
                    SELECT id 
                    FROM tipo_habitacion 
                    WHERE descripcion = %s AND hotel_id = %s
                """
                cursor.execute(query_verificacion_tipo, (descripcion_tipo, hotel_id))
                tipo_habitacion = cursor.fetchone()

                if tipo_habitacion:
                    tipo_id = tipo_habitacion[0]  # Obtenemos el ID del tipo existente
                else:
                    # Insertamos el tipo de habitación si no existe
                    query_insertar_tipo = """
                        INSERT INTO tipo_habitacion (descripcion, hotel_id)
                        VALUES (%s, %s)
                    """
                    cursor.execute(query_insertar_tipo, (descripcion_tipo, hotel_id))
                    tipo_id = cursor.lastrowid  # Obtenemos el ID del nuevo tipo

                # Insertamos la habitación asociada al tipo de habitación
                query_insertar_habitacion = """
                    INSERT INTO habitacion (numero_habitacion, tipo_id, precio)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(query_insertar_habitacion, (numero_habitacion, tipo_id, precio))

                # Confirmamos la operación
                conexion.commit()
                print("Habitación agregada correctamente.")
        except Exception as ex:
            print(f"Error al agregar habitación: {ex}")
        finally:
            if conexion:
                conexion.close()
  
    def eliminarHabitacion(self, habitacion_id):
        try:
            conexion = self.conn.obtenerConexion()
            with conexion.cursor() as cursor:
                # Verificamos que la habitación existe
                query_verificacion = """
                    SELECT tipo_id 
                    FROM habitacion
                    WHERE id = %s
                """
                cursor.execute(query_verificacion, (habitacion_id,))
                resultado = cursor.fetchone()
                if not resultado:
                    print(f"La habitación con ID {habitacion_id} no existe.")
                    return
                
                tipo_id = resultado[0]  # Obtenemos el tipo de habitación asociado
                
                # Eliminamos la habitación
                query_eliminar_habitacion = """
                    DELETE FROM habitacion
                    WHERE id = %s
                """
                cursor.execute(query_eliminar_habitacion, (habitacion_id,))
                
                # Verificar si hay más habitaciones asociadas a este tipo
                query_verificar_tipo = """
                    SELECT COUNT(*) 
                    FROM habitacion
                    WHERE tipo_id = %s
                """
                cursor.execute(query_verificar_tipo, (tipo_id,))
                if cursor.fetchone()[0] == 0:  # Si no hay más habitaciones de este tipo
                    # Eliminamos el tipo de habitación
                    query_eliminar_tipo = """
                        DELETE FROM tipo_habitacion
                        WHERE id = %s
                    """
                    cursor.execute(query_eliminar_tipo, (tipo_id,))
                
                # Confirmamos la eliminación
                conexion.commit()
                print(f"Habitación con ID {habitacion_id} y su tipo asociado (si no está en uso) han sido eliminados correctamente.")
        except Exception as ex:
            print(f"Error al eliminar la habitación: {ex}")
        finally:
            if conexion:
                conexion.close()


   
    def listarHabitacionesPorHotel(self, hotel_id): #metodo adicional para eliminar habitaciones
        try:
            conexion = self.conn.obtenerConexion()
            with conexion.cursor() as cursor:
                # Consulta para obtener las habitaciones del hotel 
                query = """
                    SELECT 
                    h.id, 
                    h.numero_habitacion, 
                    th.descripcion, 
                    h.precio
                    FROM habitacion h
                    JOIN tipo_habitacion th ON h.tipo_id = th.id
                    WHERE th.hotel_id = %s
                """
                cursor.execute(query, (hotel_id,))
                return cursor.fetchall()
        except Exception as ex:
            print(f"Error al listar habitaciones: {ex}")
            return []
        finally:
            if conexion:
                conexion.close()
   
