import mysql.connector 
from mysql.connector import Error

class Conexion():
    
    def __init__(self):
        self.conexion = None
        self.conectar()
        
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                db='hoteles'
            )
            if self.conexion.is_connected():
                print("Conexión exitosa")
                print("")
                
        except Error as ex:
            print(f"Error al conectar a la base de datos {ex}")
                  
    def obtenerConexion(self):
        if self.conexion is None or not self.conexion.is_connected():
            print("Error al iniciar la conexion, Intentando reconectar")
            self.conectar()
            
        return self.conexion
    
    def cerrarConexion(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("La conexión ha sido cerrada")