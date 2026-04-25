from models.servicio import Servicio


class Asesoria(Servicio):
    def __init__(self, nombre, precio, area):
        if not nombre:
            raise ValueError("El nombre del servicio de asesoría no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio de la asesoría debe ser mayor que cero.")
        if not area:
            raise ValueError("El área de asesoría no puede estar vacía.")

        super().__init__(nombre, precio)
        self.area = area

    def calcular_costo(self, horas):
        try:
            if horas <= 0:
                raise ValueError("Las horas de asesoría deben ser mayores que cero.")

            return self.precio * horas * 1.2

        except ValueError as error:
            with open("logs/app.log", "a", encoding="utf-8") as archivo:
                archivo.write(f"Error en Asesoria: {error}\n")
            raise

        finally:
            print("Proceso de cálculo de asesoría finalizado.")