from abc import ABC, abstractmethod

# Aca se crea la clase base abstracta que se aplica  para todos los tipos de servicios
class Servicio(ABC):
    """
    La clase Servicio define la estructura base para cualquier tipo de servicio 
    ofrecido (Sala, Equipo, Asesoría). Es abstracta por que se usa para obligar a sus hijas 
    a implementar métodos específicos.
    """

    def __init__(self, nombre, precio):
        """
        Aca se crea el Constructor de la clase Servicio.
        Recibe los siguientes parametros: nombre y precio.
        """
        # Aca se realizan las validaciones de ingreso de datos.
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del servicio no puede estar vacío")

        if precio <= 0:
            raise ValueError("El precio del servicio debe ser mayor a cero")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, horas):
        """
        Aca se define el método abstracto que debe ser implementado por las hijas. el cual se encarga de calcular el costo total del servicio.
        Recibe como parametro: horas.
        """
        pass
