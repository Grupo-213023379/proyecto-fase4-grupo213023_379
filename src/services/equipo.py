from models.servicio import Servicio

class Equipo(Servicio):
    """
 La clase Equipo representa un tipo de servicio dentro del sistema de reservas,
orientado al alquiler de dispositivos o equipos tecnológicos. Gestiona la información
básica del equipo, aplica validaciones para asegurar la integridad de los datos
y permite calcular el costo del servicio según el tiempo de uso.
    """

    def __init__(self, nombre, precio, tipo):
        """
        Se crea el constructor de la clase Equipo.
        Recibe los siguientes parametros: nombre, precio y tipo.
        """
        try:
            # Validaciones de entrada
            if not nombre:
                raise ValueError("El nombre del equipo no puede estar vacío")

            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")

            if not tipo:
                raise ValueError("El tipo de equipo no puede estar vacío")

            # Inicialización de la clase base
            super().__init__(nombre, precio)
            # Atributo específico de Equipo
            self.tipo = tipo

        except Exception as e:
            # Aca se hace el registro de errores en el log 
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error en creación de Equipo: {e}\n")
            raise


    def calcular_costo(self, horas):
        """
        Aca se calcula el costo total del alquiler del equipo.
        """
        try:
            # Verificación de que las horas sean válidas
            if horas <= 0:
                raise ValueError("Las horas deben ser mayores a 0")

            # Cálculo simple sin recargos
            return self.precio * horas

        except Exception as e:
            # Aca se hace el registro de errores en el log 
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error en cálculo de costo Equipo: {e}\n")
            raise

        finally:
            # Aca se muestra un mensaje de finalización de la operación.
            print("Cálculo de equipo finalizado")
