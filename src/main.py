import logging
from models.cliente import Cliente
from models.reserva import Reserva
from services.sala import Sala
from services.equipo import Equipo
from services.asesoria import Asesoria

logging.basicConfig(filename="logs/app.log", level=logging.ERROR)

def ejecutar():
    print("=== SISTEMA SOFTWARE FJ ===")

    clientes = []
    servicios = []
    reservas = []

    # ---------------- CLIENTES ----------------
    try:
        c1 = Cliente("Juan", "juan@gmail.com")
        c2 = Cliente("Maria", "maria@gmail.com")
        clientes.extend([c1, c2])

        # error intencional
        c3 = Cliente("Pedro", "correo_invalido")

    except Exception as e:
        logging.error(f"Error cliente: {e}")

    # ---------------- SERVICIOS ----------------
    try:
        s1 = Sala("Sala VIP", 100, 10)
        s2 = Equipo("Proyector", 50, "HD")
        s3 = Asesoria("Consultoria", 200, "IT")

        servicios.extend([s1, s2, s3])

    except Exception as e:
        logging.error(f"Error servicio: {e}")

    # ---------------- RESERVAS ----------------
    try:
        r1 = Reserva(clientes[0], servicios[0], 2)
        print("Costo reserva 1:", r1.confirmar())

        r2 = Reserva(clientes[1], servicios[1], 3)
        print("Costo reserva 2:", r2.confirmar())

        # error: servicio None
        r3 = Reserva(clientes[0], None, 1)
        r3.confirmar()

    except Exception as e:
        logging.error(f"Error reserva: {e}")

    print("=== FIN ===")


if __name__ == "__main__":
    ejecutar()