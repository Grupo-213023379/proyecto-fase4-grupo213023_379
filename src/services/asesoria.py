from models.servicio import Servicio

class Asesoria(Servicio):

    def __init__(self, nombre, precio, area):
        super().__init__(nombre, precio)
        self.area = area

    def calcular_costo(self, horas):
        return self.precio * horas * 1.2