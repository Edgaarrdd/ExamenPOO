from Model.TipoHabitacion import TipoHabitacion
from Services.CurrencyService import CurrencyService

class Habitacion:
    def __init__(self, id, numero_habitacion, tipo: TipoHabitacion, precio):
        self.id = id
        self.numero_habitacion = numero_habitacion  
        self.tipo = tipo
        self.precio = precio
    
    def __str__(self):
        return f" Id: {self.id} - Precio: {self.precio}"
    
        
    def mostrarDatos(self):
        # Este método muestra la información de las habitaciones - Se utiliza para la opcion 1 del menú
        print(f"Tipo: {self.tipo.descripcion} - Habitación: {self.numero_habitacion}  - Precio: ${self.precio}")

    def precioDolares(self):
        if self.precio is None:  # Si el precio no está definido
            return None
        servicio = CurrencyService()

        nuevoPrecio = round(float(self.precio) / servicio.obtenerValorDolar(),2) #lo convertí a float para evitar errores / tambien podía convertirlo a decimal con una libreria decimal
        
        return nuevoPrecio

    def mostrarDatosDolares(self):    # Este método muestra la información de las habitaciones en dólares  - Se utiliza en la oocion 6 del menú
        precio_dolares = self.precioDolares()
        if precio_dolares is None:  # Si el precio no está definido
            print(f"Tipo: {self.tipo.descripcion} - Habitación: {self.numero_habitacion}  - Precio: No definido")
        else:
            print(f"Tipo: {self.tipo.descripcion} - Habitación: {self.numero_habitacion}  - Precio: ${self.precio} - Precion en Dolares: US${precio_dolares}")