from src.models.servicio import Servicio


class Asesoria(Servicio):

    def __init__(self, nombre, precio, area):
        try:
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")
            if not area:
                raise ValueError("El área no puede estar vacía")

            super().__init__(nombre, precio)
            self.area = area

        except Exception as e:
            with open("logs/app.log", "a") as log:
                log.write(f"Error en creación de Asesoria: {e}\n")
            raise


    def calcular_costo(self, horas):
        try:
            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a 0")

            return self.precio * horas * 1.2

        except Exception as e:
            with open("logs/app.log", "a") as log:
                log.write(f"Error en cálculo de costo: {e}\n")
            raise

        finally:
            print("Cálculo de asesoría finalizado")