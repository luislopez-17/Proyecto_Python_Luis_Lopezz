import json
import random

# Función para guardar los datos de los envíos
def guardar_envios(data):
    try:
        with open('envios.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los envíos: {e}")

# Función para generar el número de guía
def generar_numero_guia():
    return random.randint(100000000, 999999999)

# Función para verificar si el cliente está registrado
def verificar_cliente(identifiying):
    try:
        with open("clientes.json", "r", encoding='utf-8') as archivo:
            data = json.load(archivo)
            for client in data:
                if client.get("id") == identifiying:
                    return True
        return False
    except (FileNotFoundError, json.JSONDecodeError):
        return False

# Menú para interactuar con las funciones
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar cliente")
        print("2. Registrar envío")
        print("3. Actualizar estado de envío")
        print("4. Verificar estado del envío")
        print("5. Modificar datos del cliente")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            # Mover la importación dentro de la función
            from registrar_clientes import registrar_clientes
            registrar_clientes()
        elif opcion == "2":
            # Mover la importación dentro de la función
            from registro_envio import Registro_envio
            Registro_envio()
        elif opcion == "3":
            # Mover la importación dentro de la función
            from actualizar_estado_envio import actualizar_estado_envio
            actualizar_estado_envio()
        elif opcion == "4":
            # Mover la importación dentro de la función
            from verificar_estado_envio import verificar_estado_envio
            verificar_estado_envio()
        elif opcion == "5":
            # Mover la importación dentro de la función
            from modificar_datos_clientes import modificar_datos_cliente
            modificar_datos_cliente()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
menu()