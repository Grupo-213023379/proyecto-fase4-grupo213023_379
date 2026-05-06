from models.servicio import Servicio

class Asesoria(Servicio):
    """
    Aca se crea La clase Asesoria que  hereda de Servicio.
    """

    def __init__(self, nombre, precio, area):
        """
        Aca se crea el Constructor de la clase Asesoria.
        Recibe los siguientes parametros: nombre, precio y area.
        """
        try:
            # Aca se realizan las validaciones de integridad para la validación de los parámetros del constructor.
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")
            if not area:
                raise ValueError("El área no puede estar vacía")

            # Se llama al constructor de la clase base (Servicio)
            super().__init__(nombre, precio)
            # Atributo propio de esta clase
            self.area = area

        except Exception as e:
            # Aca se hace el registro de errores en el log
            with open("logs/app.log", "a") as log:
                log.write(f"Error en creación de Asesoria: {e}\n")
            raise


    def calcular_costo(self, horas):
        """
        Aca se realiza la operación matemática para determinar el costo de la asesoría según el tiempo.
        Recibe como parametro: horas.
        """
        try:
            # Aca se valida que las horas sean válidas
            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a 0")

            # Cálculo: Precio * Horas * Factor de recargo 
            return self.precio * horas * 1.2

        except Exception as e:
            # Aca se hace el registro de errores en el log
            with open("logs/app.log", "a") as log:
                log.write(f"Error en cálculo de costo: {e}\n")
            raise

        finally:
            print("Cálculo de asesoría finalizado")
