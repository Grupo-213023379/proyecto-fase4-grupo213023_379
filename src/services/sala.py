from models.servicio import Servicio

# Aca se crea la clase Sala
class Sala(Servicio):
    """
    La clase Sala gestiona el alquiler de espacios para reuniones o eventos.
    """

    def __init__(self, nombre, precio, capacidad):
        """
        Aca se crea el Constructor de la clase Sala.
        Recibe los siguientes parametros: nombre, precio y capacidad.
        """
        try:
            # Validaciones básicas de integridad
            if not nombre:
                raise ValueError("El nombre de la sala no puede estar vacío")

            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")

            if capacidad <= 0:
                raise ValueError("La capacidad debe ser mayor a 0")

            # Invocación al constructor heredado de Servicio
            super().__init__(nombre, precio)
            # Propiedad específica de la Sala
            self.capacidad = capacidad

        except Exception as e:
            # Aca se hace el registro de errores en el log
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error en creación de Sala: {e}\n")
            raise


    def calcular_costo(self, horas):
        """
        Aca se realiza la operación matemática para determinar el costo según el tiempo.
        Recibe como parametro: horas.
        """
        try:
            # El tiempo de reserva debe ser coherente
            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a 0")

            # Lógica de cobro base
            return self.precio * horas

        except Exception as e:
            # Aca se hace el registro de errores en el log
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error en cálculo de costo Sala: {e}\n")
            raise

        finally:
            # Aca se muestra un mensaje de finalización de la operación.
            print("Cálculo de sala finalizado")
