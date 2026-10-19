import os

lista_trabajadores = [
    {"id": "A001", "pase": "1234", "cargo": "Administrador", "nombre": "Marcelo Bendezú"},
    {"id": "A002", "pase": "5678", "cargo": "Asistente", "nombre": "Ana Sulca"}
]

lista_expedientes = []
ARCHIVO_DATOS = "expedientes.txt"

def cargar_expedientes():
    if os.path.exists(ARCHIVO_DATOS):
        archivo = open(ARCHIVO_DATOS, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
        
        for linea in lineas:
            datos = linea.strip().split(";")
            if len(datos) == 8:
                expediente = {
                    "codigo": datos[0],
                    "fecha": datos[1],
                    "nombre": datos[2],
                    "dni": datos[3],
                    "tipo_doc": datos[4],
                    "asunto": datos[5],
                    "area": datos[6],
                    "estado": datos[7]
                }
                lista_expedientes.append(expediente)

def guardar_expedientes():
    archivo = open(ARCHIVO_DATOS, "w", encoding="utf-8")
    for exp in lista_expedientes:
        linea = exp['codigo'] + ";" + exp['fecha'] + ";" + exp['nombre'] + ";" + exp['dni'] + ";" + exp['tipo_doc'] + ";" + exp['asunto'] + ";" + exp['area'] + ";" + exp['estado'] + "\n"
        archivo.write(linea)
    archivo.close()
    print(">> Datos guardados correctamente en el archivo.")

def validar_credenciales(id_ingresado, pase_ingresado):
    for trabajador in lista_trabajadores:
        if trabajador["id"] == id_ingresado and trabajador["pase"] == pase_ingresado:
            return trabajador
    return None

def iniciar_sesion():
    print("========================================")
    print(" SIDESP - MESA DE PARTES DIGITAL (UPN)  ")
    print("========================================")
    while True:
        id_ingresado = input("Ingrese ID de trabajador: ")
        pase_ingresado = input("Ingrese contraseña: ")
        trabajador = validar_credenciales(id_ingresado, pase_ingresado)
        
        if trabajador is not None:
            print("\n¡Bienvenido, " + trabajador['nombre'] + " (" + trabajador['cargo'] + ")!")
            return trabajador
        else:
            print("Credenciales incorrectas. Intente nuevamente.\n")

def registrar_expediente():
    print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---")
    
    total_exp = len(lista_expedientes) + 1
    codigo = "EXP-00" + str(total_exp)
    
    fecha = input("Ingrese fecha de registro (ej. 18/10/2026): ")
    if fecha == "":
        fecha = "18/10/2026"
    
    nombre = input("Ingrese nombre completo del ciudadano: ")
    
    print("Seleccione tipo de documento:")
    print("1. Solicitud")
    print("2. Oficio")
    print("3. Carta")
    op_tipo = input("Elija una opción (1-3): ")
    
    tipo_doc = "Solicitud"
    if op_tipo == "2":
        tipo_doc = "Oficio"
    elif op_tipo == "3":
        tipo_doc = "Carta"
    
    dni = input("Ingrese número de DNI (8 dígitos): ")
    while len(dni) != 8 or not dni.isdigit():
        print("DNI inválido. Debe contener exactamente 8 dígitos numéricos.")
        dni = input("Ingrese número de DNI (8 dígitos): ")
        
    asunto = input("Ingrese asunto del expediente: ")
    area = input("Ingrese área de destino (ej. Tecnología de la Información): ")
    estado = "Registrado"
    
    expediente = {
        "codigo": codigo,
        "fecha": fecha,
        "nombre": nombre,
        "dni": dni,
        "tipo_doc": tipo_doc,
        "asunto": asunto,
        "area": area,
        "estado": estado
    }
    
    lista_expedientes.append(expediente)
    guardar_expedientes()
    print("Expediente registrado correctamente. Código asignado: " + codigo)

def consultar_expediente():
    print("\n--- CONSULTA DE EXPEDIENTES ---")
    if len(lista_expedientes) == 0:
        print("No hay expedientes registrados en el sistema.")
        return
        
    criterio = input("Ingrese el Código (ej. EXP-001) o DNI a buscar: ")
    encontrado = False
    
    for exp in lista_expedientes:
        if exp["codigo"] == criterio or exp["dni"] == criterio:
            print("\n--- DETALLE DEL EXPEDIENTE ---")
            print("Código          : " + exp['codigo'])
            print("Fecha           : " + exp['fecha'])
            print("Ciudadano       : " + exp['nombre'])
            print("DNI             : " + exp['dni'])
            print("Tipo de Doc.    : " + exp['tipo_doc'])
            print("Asunto          : " + exp['asunto'])
            print("Área de Destino : " + exp['area'])
            print("Estado          : " + exp['estado'])
            encontrado = True
            break
            
    if not encontrado:
        print("Expediente no encontrado.")

def modificar_expediente():
    print("\n--- MODIFICACIÓN DE EXPEDIENTE ---")
    if len(lista_expedientes) == 0:
        print("No hay expedientes registrados.")
        return
        
    codigo = input("Ingrese el código del expediente a modificar: ")
    expediente_encontrado = None
    
    for exp in lista_expedientes:
        if exp["codigo"] == codigo:
            expediente_encontrado = exp
            break
            
    if expediente_encontrado is None:
        print("Expediente no encontrado.")
        return
        
    print("Seleccione el dato que desea modificar:")
    print("1. Datos del usuario (Nombre / DNI)")
    print("2. Asunto a responder")
    opcion = input("Elija una opción (1-2): ")
    
    if opcion == "1":
        nuevo_nombre = input("Nuevo nombre: ")
        if nuevo_nombre != "":
            expediente_encontrado["nombre"] = nuevo_nombre
        nuevo_dni = input("Nuevo DNI: ")
        if len(nuevo_dni) == 8 and nuevo_dni.isdigit():
            expediente_encontrado["dni"] = nuevo_dni
        print("Datos del usuario actualizados.")
    elif opcion == "2":
        nuevo_asunto = input("Nuevo asunto: ")
        if nuevo_asunto != "":
            expediente_encontrado["asunto"] = nuevo_asunto
        print("Asunto actualizado.")
    else:
        print("Opción no válida.")
        return
        
    guardar_expedientes()
    print("Expediente modificado correctamente.")

def ordenar_expedientes():
    print("\n--- LISTADO GENERAL DE EXPEDIENTES ---")
    if len(lista_expedientes) == 0:
        print("No hay expedientes registrados.")
        return
        
    lista_ordenada = sorted(lista_expedientes, key=lambda x: x["codigo"])
    
    print("CÓDIGO     | FECHA      | CIUDADANO            | TIPO       | ESTADO")
    print("-" * 68)
    for exp in lista_ordenada:
        print(exp['codigo'] + " | " + exp['fecha'] + " | " + exp['nombre'] + " | " + exp['tipo_doc'] + " | " + exp['estado'])

def mostrar_menu_restringido():
    while True:
        print("\n=== MENÚ PRINCIPAL (CARGO: ASISTENTE) ===")
        print("1. Registrar expediente")
        print("2. Consultar expediente")
        print("3. Listar expedientes")
        print("4. Cerrar sesión")
        op = input("Seleccione una opción: ")
        
        if op == "1":
            registrar_expediente()
        elif op == "2":
            consultar_expediente()
        elif op == "3":
            ordenar_expedientes()
        elif op == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")

def mostrar_menu_completo():
    while True:
        print("\n=== MENÚ PRINCIPAL (CARGO: ADMINISTRADOR) ===")
        print("1. Registrar expediente")
        print("2. Consultar expediente")
        print("3. Modificar expediente")
        print("4. Listar expedientes")
        print("5. Cerrar sesión")
        op = input("Seleccione una opción: ")
        
        if op == "1":
            registrar_expediente()
        elif op == "2":
            consultar_expediente()
        elif op == "3":
            modificar_expediente()
        elif op == "4":
            ordenar_expedientes()
        elif op == "5":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")

def main():
    cargar_expedientes()
    while True:
        trabajador = iniciar_sesion()
        if trabajador["cargo"] == "Administrador":
            mostrar_menu_completo()
        elif trabajador["cargo"] == "Asistente":
            mostrar_menu_restringido()
            
        continuar = input("\n¿Desea ingresar con otro usuario? (s/n): ")
        if continuar.lower() != 's':
            print("¡Gracias por utilizar el sistema!")
            break

if __name__ == "__main__":
    main()