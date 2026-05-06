# Aca se crea la clase que representa a un cliente 
class Cliente:
    """
    La clase Cliente permite almacenar y gestionar la información básica de los usuarios.
    Incluye validaciones para asegurar que los datos ingresados sean correctos.
    """

    def __init__(self, nombre, correo):
        """
         Aca se crea el Constructor de la clase Cliente.
         Recibe los siguientes parametros: nombre y correo.
        """
        try:
            # Aca se realiza la validación de integridad para la validación de los parámetros del constructor.
            if not nombre or nombre.strip() == "":
                raise ValueError("El nombre del cliente no puede estar vacío")

            # Aca se realiza la validación de integridad para la validación de los parámetros del constructor.
            if "@" not in correo or "." not in correo:
                raise ValueError("El correo ingresado no es válido")

            # Aca se asignan los atributos privados para proteger la información (Encapsulamiento)
            self.__nombre = nombre
            self.__correo = correo

        except Exception as e:
            # Si ocurre un error, se registra en el archivo de log 
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error al crear cliente: {e}\n")
            # Se vuelve a lanzar la excepción para que el programa principal la maneje
            raise

    def obtener_nombre(self):
        """
        Metodo 'getter' para obtener el nombre del cliente de forma segura.
        """
        return self.__nombre

    def obtener_correo(self):
        """
        Metodo 'getter' para obtener el correo del cliente de forma segura.
        """
        return self.__correo

    def mostrar_info(self):
        """
        Aca se muestra la información del cliente.
        """
        return f"Cliente: {self.__nombre} - Correo: {self.__correo}"
