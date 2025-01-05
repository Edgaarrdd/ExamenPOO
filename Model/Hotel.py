
class Hotel:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = [] 
      
    def __str__(self):
        return f"Nombre del Hotel: {self.nombre} - Direccion: {self.direccion}"
    
    def mostrarDatos(self):
        print(f"{self.nombre} - Dirección: {self.direccion}")
        if self.habitaciones:  # Verificamos si hay habitaciones asociadas
            for habitacion in self.habitaciones:
                habitacion.mostrarDatos() #llamamos al metodo mostrarDatos de la clase Habitacion
        else:
            print("  No hay habitaciones asociadas.")
    
    def agregarHabitacionHotel(self):
        print(f"id:{self.id}  Hotel: {self.nombre}")
        
    def mostrarDatosDolares(self):
        print(f"{self.nombre} - Dirección: {self.direccion}")
        if self.habitaciones:  # Verificamos si hay habitaciones asociadas
            for habitacion in self.habitaciones:
                habitacion.mostrarDatosDolares() #llamamos al metodo mostrarDatos de la clase Habitacion
        else:
            print("  No hay habitaciones asociadas.")
            
            