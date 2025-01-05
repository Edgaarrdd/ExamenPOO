from Model.Hotel import Hotel

class TipoHabitacion:
    
    def __init__(self, id, descripcion, hotel: Hotel):
        self.id = id
        self.descripcion = descripcion
        self.hotel = hotel

    def __str__(self):
        return f"ID:{self.id} El tipo de habitación es: {self.descripcion}"
    
    def mostrarDatos(self):
        print(f"ID:{self.id} - Tipo de Habitación: {self.descripcion} - Hotel: {self.hotel.nombre}")
    
    def menuTiposHabitacion(self):
        return f"Tipo habitación: {self.descripcion}"