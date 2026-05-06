#  Aca se crea la clase Reserva que gestiona las reservas de los servicios por parte de los clientes
class Reserva:
    """
    Aca se define la clase Reserva donde se vincula a un Cliente con un Servicio específico durante un tiempo determinado.
    Se maneja el flujo de estados (pendiente, confirmada, cancelada).
    """

    def __init__(self, cliente, servicio, horas):
        """
         Aca se crea el Constructor de la clase Reserva.
        """
        try:
            # Aca se realizan las validaciones de los campos del constructor
            if cliente is None:
                raise ValueError("El cliente no puede estar vacío")

            if servicio is None:
                raise ValueError("El servicio no puede estar vacío")

            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a cero")

            # Aca se hace la asignación de los atributos iniciales
            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "pendiente" # La reserva nace en estado pendiente

        except Exception as e:
            # Aca se hace el registro de errores en el log
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error al crear reserva: {e}\n")
            raise

    def confirmar(self):
        """
        Aca se confirma la reserva, se calcula el costo total y se cambia su estado.
        """
        try:
            # Aca se valida que no se puede confirmar una reserva ya confirmada
            if self.estado == "confirmada":
                raise Exception("La reserva ya fue confirmada")

            # Aca se aplica polimorfismo: se llama a calcular_costo() del servicio específico
            costo = self.servicio.calcular_costo(self.horas)
            self.estado = "confirmada"
            return costo

        except Exception as e:
            # Aca se hace el registro de errores en el log
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error al confirmar reserva: {e}\n")
            raise

        finally:
            # Aca se imprime siempre que se ejecute el proceso de confirmacion de reserva
            print("Proceso de confirmación de reserva finalizado")

    def cancelar(self):
        """
        Aca se cancela una reserva existente y cambia su estado.
        """
        try:
            # Aca se valida que no se puede cancelar una reserva ya cancelada
            if self.estado == "cancelada":
                raise Exception("La reserva ya fue cancelada")

            self.estado = "cancelada"
            return "Reserva cancelada correctamente"

        except Exception as e:
            # Aca se hace el registro de errores en el log
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error al cancelar reserva: {e}\n")
            raise
