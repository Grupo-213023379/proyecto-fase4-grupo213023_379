class Cliente:
    def __init__(self, nombre, correo):
        if "@" not in correo:
            raise ValueError("Correo inválido")

        self._nombre = nombre
        self._correo = correo