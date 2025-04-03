import json

# Función para verificar el estado del pedido
def verificar_estado_envio():
    # Solicitar el número de guía y validar que sea un número entero
    while True:
        try:
            numero_guia = int(input("Ingrese el número de guía para verificar el estado: "))
            break  # Salir del bucle si la conversión es exitosa
        except ValueError:
            print("Por favor, ingrese un número de guía válido (solo números).")

    try:
        # Leer los datos de los envíos desde el archivo
        with open("envios.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

        # Buscar el envío con el número de guía y mostrar el estado
        for envio in data:
            if envio.get("numero de guia") == numero_guia:
                print(f"\nEstado del envío con número de guía {numero_guia}: {envio['estado']}")
                return  # Terminar la función después de encontrar el envío

        # Si no se encuentra el número de guía
        print("No se encontró un envío con ese número de guía.")
    
    except FileNotFoundError:
        print("El archivo 'envios.json' no se encontró. Asegúrese de que exista y esté correctamente ubicado.")
    except json.JSONDecodeError:
        print("Hubo un error al leer el archivo de envíos. Asegúrese de que el archivo esté en el formato correcto.")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")