# Módulo para el manejo de archivos de texto

def cargar_expedientes(nombre_archivo):
    expedientes = []
    f = open(nombre_archivo, 'r')
    lineas = f.readlines()
    f.close()
    for linea in lineas:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(',')
            expedientes.append(partes)
    return expedientes

def guardar_expedientes(nombre_archivo, expedientes):
    f = open(nombre_archivo, 'w')
    for exp in expedientes:
        linea = exp[0] + "," + exp[1] + "," + exp[2] + "," + exp[3] + "," + exp[4] + "\n"
        f.write(linea)
    f.close()