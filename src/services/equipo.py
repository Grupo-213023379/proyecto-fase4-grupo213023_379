from models.servicio import Servicio

class Equipo(Servicio):

    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def calcular_costo(self, horas):
        return self.precio * horas