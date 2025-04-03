import json
from proyecto import guardar_envios

def actualizar_estado_envio():
    # Solicitar el número de guía y el nuevo estado
    while True:
        try:
            numero_guia = int(input("Ingrese el número de guía del envío a actualizar: "))
            break  # Si la conversión es exitosa, salimos del bucle
        except ValueError:
            print("Por favor, ingrese un número de guía válido.")

    nuevo_estado = input("Ingrese el nuevo estado del envío (Ej. En tránsito, Entregado, etc.): ")

    try:
        # Leer los datos de los envíos desde el archivo
        with open("envios.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

        # Buscar el envío con el número de guía y actualizar su estado
        for envio in data:
            if envio.get("numero de guia") == numero_guia:
                envio["estado"] = nuevo_estado
                break
        else:
            print("No se encontró un envío con ese número de guía.")
            return

        # Guardar los cambios en el archivo JSON
        try:
            guardar_envios(data)  # Función encargada de guardar los envíos
            print(f"El estado del envío con número de guía {numero_guia} ha sido actualizado a '{nuevo_estado}'.")
        except Exception as e:
            print(f"Error al guardar el estado actualizado: {e}")

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al acceder a los envíos: {e}")