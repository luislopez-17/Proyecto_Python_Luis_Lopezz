import json

def registrar_clientes():
    print("---------- Registro de Cliente ----------")
    
    # Recolección de datos
    name = input("Nombres: ").title()
    surname = input("Apellidos: ").title()
    type_identification = input("Tipo de identificación (CC, TI, CE): ")
    identifiying = input("Número de identificación: ")
    direction = input("Dirección: ")
    
    # Validación de teléfono fijo y celular (solo números)
    while True:
        try:
            fixed_telephone = int(input("Teléfono fijo: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el teléfono fijo.")
    
    while True:
        try:
            cellular = int(input("Número de celular: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el celular.")
    
    residence = input("Barrio de residencia: ").title()

    # Crear un diccionario con los datos del cliente
    client = {
        'nombre': name,
        'apellido': surname,
        'tipo_de_id': type_identification,
        'id': identifiying,
        'direccion': direction,
        'telefono_fijo': fixed_telephone,
        'celular': cellular,
        'residencia': residence
    }

    # Leer los clientes existentes desde el archivo JSON
    try:
        with open('clientes.json', 'r+', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []  # Si el archivo está vacío o corrupto
    except FileNotFoundError:
        data = []

    # Verificar si el cliente ya está registrado (evitar duplicados)
    for existing_client in data:
        if existing_client['id'] == identifiying:
            print(f"Ya existe un cliente registrado con el número de identificación {identifiying}.")
            return  # Salir de la función si el cliente ya está registrado

    # Agregar el nuevo cliente a la lista de clientes
    data.append(client)

    # Guardar los datos actualizados de los clientes en el archivo
    try:
        with open('clientes.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("\nCliente registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar el cliente: {e}")