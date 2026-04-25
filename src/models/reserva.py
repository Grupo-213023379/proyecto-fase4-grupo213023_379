class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            if cliente is None:
                raise ValueError("El cliente no puede estar vacío")

            if servicio is None:
                raise ValueError("El servicio no puede estar vacío")

            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a cero")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "pendiente"

        except Exception as e:
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error al crear reserva: {e}\n")
            raise

    def confirmar(self):
        try:
            if self.estado == "confirmada":
                raise Exception("La reserva ya fue confirmada")

            costo = self.servicio.calcular_costo(self.horas)
            self.estado = "confirmada"
            return costo

        except Exception as e:
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error al confirmar reserva: {e}\n")
            raise

        finally:
            print("Proceso de confirmación de reserva finalizado")

    def cancelar(self):
        try:
            if self.estado == "cancelada":
                raise Exception("La reserva ya fue cancelada")

            self.estado = "cancelada"
            return "Reserva cancelada correctamente"

        except Exception as e:
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error al cancelar reserva: {e}\n")
            raise