# Módulo de funciones principales del sistema de Mesa de Partes

def mostrar_menu():
    print("\n--- SISTEMA DE MESA DE PARTES DIGITAL ---")
    print("1. Registrar nuevo expediente")
    print("2. Ver expedientes registrados")
    print("3. Buscar expediente")
    print("4. Salir")

def registrar_expediente(expedientes):
    print("\n--- REGISTRAR EXPEDIENTE ---")
    codigo = input("Ingrese código del expediente: ")
    remitente = input("Ingrese nombre del remitente: ")
    dni = input("Ingrese DNI: ")
    asunto = input("Ingrese asunto: ")
    estado = "En trámite"
    
    nuevo = [codigo, remitente, dni, asunto, estado]
    expedientes.append(nuevo)
    print("¡Expediente registrado con éxito!")

def ver_expedientes(expedientes):
    print("\n--- LISTA DE EXPEDIENTES ---")
    if len(expedientes) == 0:
        print("No hay expedientes registrados.")
    else:
        for exp in expedientes:
            print(f"Código: {exp[0]} | Remitente: {exp[1]} | DNI: {exp[2]} | Asunto: {exp[3]} | Estado: {exp[4]}")

def buscar_expediente(expedientes):
    print("\n--- BUSCAR EXPEDIENTE ---")
    codigo_buscar = input("Ingrese el código a buscar: ")
    encontrado = False
    for exp in expedientes:
        if exp[0] == codigo_buscar:
            print(f"¡Encontrado! -> Remitente: {exp[1]}, Asunto: {exp[3]}, Estado: {exp[4]}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún expediente con ese código.")