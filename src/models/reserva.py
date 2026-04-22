class Reserva:

    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "pendiente"

    def confirmar(self):
        if self.servicio is None:
            raise Exception("Servicio no válido")

        costo = self.servicio.calcular_costo(self.horas)
        self.estado = "confirmada"
        return costo