from models.servicio import Servicio


class Sala(Servicio):

    def __init__(self, nombre, precio, capacidad):
        try:
            if not nombre:
                raise ValueError("El nombre de la sala no puede estar vacío")

            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")

            if capacidad <= 0:
                raise ValueError("La capacidad debe ser mayor a 0")

            super().__init__(nombre, precio)
            self.capacidad = capacidad

        except Exception as e:
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error en creación de Sala: {e}\n")
            raise


    def calcular_costo(self, horas):
        try:
            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a 0")

            return self.precio * horas

        except Exception as e:
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error en cálculo de costo Sala: {e}\n")
            raise

        finally:
            print("Cálculo de sala finalizado")