import json

# Función para registrar un envío
def Registro_envio():
    print("-------- REGISTRO DE ENVÍO --------")

    # Identificar al remitente
    identifiying = input("Ingrese número de ID: ")
    
    # Mover la importación a este punto, justo cuando se necesite
    from proyecto import verificar_cliente, generar_numero_guia, guardar_envios

    if not verificar_cliente(identifiying):
        print("\nEl cliente no está registrado.")
        return  # Salir si el cliente no está registrado
    else:
        print("Cliente verificado con éxito. Procediendo con el registro del envío...")

        # Datos del destinatario
        NAME_OF_RECIPIENT = input("Nombre del destinatario: ").title()
        ADDRESS_RECIPIENT = input("Dirección del destinatario: ")
        TELEPHONE_RECIPIENT = input("Teléfono del destinatario: ")
        CITY_RECIPIENT = input("Ciudad del destinatario: ").title()
        NEIGHBOURHOOD_RECIPIENT = input("Barrio del destinatario: ").title()

        # Validación de fecha
        DATE = input("Fecha de envío (DD/MM/AAAA): ")
        while not validar_fecha(DATE):
            print("Formato de fecha incorrecto. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")
            DATE = input("Fecha de envío (DD/MM/AAAA): ")

        HOUR = input("Hora de envío: ")

        # Generación del número de guía
        numero_guia = generar_numero_guia()
        print(f"El número de guía de su envío es: {numero_guia}")

        STATE_OF_DISPATCH = "RECIBIDO"

        ENVIO = {
            'FECHA': DATE,
            'HORA': HOUR,
            'DESTINATARIO': {
                'NOMBRE': NAME_OF_RECIPIENT,
                'DIRECCION': ADDRESS_RECIPIENT,
                'TELEFONO': TELEPHONE_RECIPIENT,
                'CIUDAD': CITY_RECIPIENT,
                'BARRIO': NEIGHBOURHOOD_RECIPIENT
            },
            'numero de guia': numero_guia,
            'estado': STATE_OF_DISPATCH
        }

        # Leer los envíos existentes desde el archivo JSON
        try:
            with open('envios.json', 'r+', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []  # Si el archivo está vacío o corrupto
        except FileNotFoundError:
            data = []

        # Agregar el nuevo envío
        data.append(ENVIO)

        # Guardar los datos actualizados de los envíos
        try:
            guardar_envios(data)
            print("\nEnvío registrado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el envío: {e}")


# Función para validar el formato de la fecha
def validar_fecha(fecha):
    """Verifica si la fecha tiene el formato DD/MM/AAAA."""
    try:
        day, month, year = map(int, fecha.split('/'))
        # Comprobar que el mes esté entre 1 y 12 y el día válido en el mes
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
        return False
    except ValueError:
        return False