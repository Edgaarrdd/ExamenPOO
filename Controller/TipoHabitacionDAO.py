from Database.Conexion import Conexion
from Model.Hotel import Hotel
from Model.TipoHabitacion import TipoHabitacion

class TipoHabitacionDAO:
    
    def __init__(self):
        self.conn = Conexion()
        
    def obtenerTiposHabitacion(self):
      
        #Consulta y retorna una lista de tipos de habitación con sus IDs y descripciones.
        try:
            conexion = self.conn.obtenerConexion()
            with conexion.cursor() as cursor:
                cursor.execute("""SELECT DISTINCT
                            h.id as hotel_id,
                            h.nombre AS hotel_nombre,
                            h.direccion AS hotel_direccion,
                            th.id AS tipo_id,
                            th.descripcion AS tipo_habitacion
                        FROM hotel h
                        JOIN tipo_habitacion th ON h.Id = th.hotel_id
                        GROUP by th.descripcion
                        """)
            
                listado = cursor.fetchall()
                tipos = []
                
                for tipo in listado:
                    tipoHabitacion = TipoHabitacion(tipo[3], tipo[4],Hotel)
                    hotel = Hotel(tipo[0], tipo[1],tipo[2])
                    
                    tipos.append(tipoHabitacion)
                return tipos
        except Exception as ex:
            print(f"Error al obtener tipos de habitación: {ex}")
            return []
        finally:
            if conexion:
                conexion.close()
                
    def listarTiposHabitacion(self):
        try:
            conexion = self.conn.obtenerConexion()
            with conexion.cursor() as cursor:
                # Consulta para obtener los tipos de habitación
                query = """SELECT DISTINCT 
                        id, 
                        descripcion 
                        FROM tipo_habitacion
                        GROUP BY descripcion
                        """
                cursor.execute(query)
                tipos = cursor.fetchall()
                return tipos
        except Exception as ex:
            print(f"Error al listar tipos de habitación: {ex}")
            return []
        finally:
            if conexion:
                conexion.close()           