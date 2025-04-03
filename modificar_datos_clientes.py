import json

# Función para modificar los datos del cliente
def modificar_datos_cliente():
    identifiying = input("Ingrese el número de ID del cliente que desea modificar: ")

    try:
        # Leer los datos de los clientes desde el archivo JSON
        with open("clientes.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

        # Buscar el cliente con el número de ID
        for client in data:
            if client.get("id") == identifiying:
                print(f"\nCliente encontrado: {client['nombre']} {client['apellido']}")

                # Solicitar y validar los nuevos datos
                new_address = input("Nueva dirección: ").strip()
                while not new_address:
                    print("La dirección no puede estar vacía. Intente nuevamente.")
                    new_address = input("Nueva dirección: ").strip()

                # Validar que el teléfono fijo sea un número
                while True:
                    try:
                        new_fixed_telephone = int(input("Nuevo teléfono fijo: "))
                        break  # Salir si es un número válido
                    except ValueError:
                        print("Por favor, ingrese un número válido para el teléfono fijo.")

                # Validar que el número de celular sea un número
                while True:
                    try:
                        new_cellular = int(input("Nuevo número de celular: "))
                        break  # Salir si es un número válido
                    except ValueError:
                        print("Por favor, ingrese un número válido para el celular.")
                
                # Actualizar los datos del cliente
                client['direccion'] = new_address
                client['telefono_fijo'] = new_fixed_telephone
                client['celular'] = new_cellular

                print("Datos del cliente actualizados exitosamente.")
                break
        else:
            print("No se encontró un cliente con ese número de identificación.")
            return

        # Guardar los cambios en el archivo JSON
        with open("clientes.json", "w", encoding="utf-8") as archivo:
            json.dump(data, archivo, indent=4, ensure_ascii=False)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al acceder a los clientes: {e}")