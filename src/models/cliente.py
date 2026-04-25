class Cliente:
    def __init__(self, nombre, correo):
        try:
            if not nombre or nombre.strip() == "":
                raise ValueError("El nombre del cliente no puede estar vacío")

            if "@" not in correo or "." not in correo:
                raise ValueError("El correo ingresado no es válido")

            self.__nombre = nombre
            self.__correo = correo

        except Exception as e:
            with open("logs/app.log", "a", encoding="utf-8") as log:
                log.write(f"Error al crear cliente: {e}\n")
            raise

    def obtener_nombre(self):
        return self.__nombre

    def obtener_correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - Correo: {self.__correo}"