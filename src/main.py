# Importación del módulo logging para registrar errores en un archivo
import logging

# Importación de las clases del sistema
from models.cliente import Cliente
from models.reserva import Reserva
from services.sala import Sala
from services.equipo import Equipo
from services.asesoria import Asesoria


# Configuración del sistema de logs
logging.basicConfig(
    filename="logs/app.log", # archivo donde se guardan los errores
    level=logging.ERROR, # solo se guardan errores
    format="%(asctime)s - %(levelname)s - %(message)s", # formato del mensaje
    encoding="utf-8" # para evitar errores con caracteres especiales
)


# mostrar títulos en consola
def mostrar_titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


# Función general para ejecutar las operaciones con el control de errores
def ejecutar_operacion(numero, descripcion, funcion):
    print(f"\nOperación {numero}: {descripcion}")

    try:
        # Se ejecuta la función enviada como parámetro
        resultado = funcion()

    except Exception as error:
        # Si ocurre un error, se registra en el log
        logging.error(f"Operación {numero} fallida: {error}")

        # Se muestra el error en pantalla de forma controlada
        print(f"Error controlado: {error}")
        print("El error fue registrado en logs/app.log")

    else:
        # Si no hay errores, se indica éxito
        print("Operación exitosa")

        # Si la función retorna algo, se muestra
        if resultado is not None:
            print(f"Resultado: {resultado}")

    finally:
        # Siempre se ejecuta al final (con o sin error)
        print("Proceso finalizado")


# Función principal del sistema
def ejecutar():

    # Listas para almacenar los objetos creados
    clientes = []
    servicios = []
    reservas = []

    # Título inicial
    mostrar_titulo("SISTEMA INTEGRAL SOFTWARE FJ")


    # ------------------- CLIENTES -------------------

    ejecutar_operacion(
        1,
        "Registrar cliente válido",
        # Se crea un cliente correcto y se agrega a la lista
        lambda: clientes.append(Cliente("Juan Pérez", "juan@gmail.com")) or "Cliente Juan registrado"
    )

    ejecutar_operacion(
        2,
        "Registrar segundo cliente válido",
        lambda: clientes.append(Cliente("María López", "maria@gmail.com")) or "Cliente María registrada"
    )

    ejecutar_operacion(
        3,
        "Intentar registrar cliente con correo inválido",
        # Aquí se genera un error intencional
        lambda: clientes.append(Cliente("Pedro Gómez", "correo_invalido"))
    )


    # ------------------- SERVICIOS -------------------

    ejecutar_operacion(
        4,
        "Crear servicio de sala válido",
        lambda: servicios.append(Sala("Sala VIP", 100, 10)) or "Servicio Sala VIP creado"
    )

    ejecutar_operacion(
        5,
        "Crear servicio de equipo válido",
        lambda: servicios.append(Equipo("Proyector", 50, "HD")) or "Servicio Proyector creado"
    )

    ejecutar_operacion(
        6,
        "Crear servicio de asesoría válido",
        lambda: servicios.append(Asesoria("Consultoría", 200, "IT")) or "Servicio Consultoría creado"
    )

    ejecutar_operacion(
        7,
        "Intentar crear servicio con precio inválido",
        # Error intencional: precio negativo
        lambda: servicios.append(Sala("Sala dañada", -100, 5))
    )


    # ------------------- RESERVAS -------------------

    ejecutar_operacion(
        8,
        "Crear y confirmar reserva de sala",
        # Se crea la reserva y se calcula el costo
        lambda: reservas.append(Reserva(clientes[0], servicios[0], 2)) or 
                f"Costo reserva sala: {Reserva(clientes[0], servicios[0], 2).confirmar()}"
    )

    ejecutar_operacion(
        9,
        "Crear y confirmar reserva de equipo",
        lambda: reservas.append(Reserva(clientes[1], servicios[1], 3)) or 
                f"Costo reserva equipo: {Reserva(clientes[1], servicios[1], 3).confirmar()}"
    )

    ejecutar_operacion(
        10,
        "Intentar crear reserva con servicio no válido",
        # Error intencional: servicio None
        lambda: Reserva(clientes[0], None, 1).confirmar()
    )


    mostrar_titulo("RESUMEN FINAL")

    # Se muestran estadísticas del sistema
    print(f"Clientes registrados correctamente: {len(clientes)}")
    print(f"Servicios creados correctamente: {len(servicios)}")
    print(f"Reservas almacenadas correctamente: {len(reservas)}")

    print("Los errores controlados quedaron registrados en logs/app.log")
    print("=== FIN DEL SISTEMA ===")

if __name__ == "__main__":
    ejecutar()