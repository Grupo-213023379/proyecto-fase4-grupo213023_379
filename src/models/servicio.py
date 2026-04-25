from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del servicio no puede estar vacío")

        if precio <= 0:
            raise ValueError("El precio del servicio debe ser mayor a cero")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, horas):
        pass