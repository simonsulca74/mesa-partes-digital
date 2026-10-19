# Archivo principal del Sistema de Mesa de Partes Digital
from datos import cargar_expedientes, guardar_expedientes
from funciones import mostrar_menu, registrar_expediente, ver_expedientes, buscar_expediente

def main():
    # Archivo de texto donde se guardan los datos
    archivo_datos = "expedientes.txt"
    
    # Cargamos los expedientes existentes al iniciar el programa
    try:
        expedientes = cargar_expedientes(archivo_datos)
    except:
        expedientes = []

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            registrar_expediente(expedientes)
            guardar_expedientes(archivo_datos, expedientes)
        elif opcion == "2":
            ver_expedientes(expedientes)
        elif opcion == "3":
            buscar_expediente(expedientes)
        elif opcion == "4":
            print("\n¡Gracias por usar el Sistema de Mesa de Partes Digital. Hasta luego!")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()