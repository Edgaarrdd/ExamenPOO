import requests

class CurrencyService:
    def __init__(self):
        self.api_url = "https://mindicador.cl/api/dolar"
        
    def obtenerValorDolar(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            
            dolar = data['serie'][0]['valor']
            return dolar
            
        except(requests.RequestException, KeyError) as ex:
            print(f"Error al obtener el valor del dolar: {ex}")
            return 1