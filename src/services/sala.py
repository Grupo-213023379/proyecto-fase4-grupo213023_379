from models.servicio import Servicio

class Sala(Servicio):

    def __init__(self, nombre, precio, capacidad):
        super().__init__(nombre, precio)
        self.capacidad = capacidad

    def calcular_costo(self, horas):
        return self.precio * horas