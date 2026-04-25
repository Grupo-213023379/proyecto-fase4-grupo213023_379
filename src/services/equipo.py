from models.servicio import Servicio


class Equipo(Servicio):

    def __init__(self, nombre, precio, tipo):
        try:
            if not nombre:
                raise ValueError("El nombre del equipo no puede estar vacío")

            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")

            if not tipo:
                raise ValueError("El tipo de equipo no puede estar vacío")

            super().__init__(nombre, precio)
            self.tipo = tipo

        except Exception as e:
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error en creación de Equipo: {e}\n")
            raise


    def calcular_costo(self, horas):
        try:
            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a 0")

            return self.precio * horas

        except Exception as e:
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error en cálculo de costo Equipo: {e}\n")
            raise

        finally:
            print("Cálculo de equipo finalizado")