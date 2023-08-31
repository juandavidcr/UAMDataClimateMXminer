import os
def buscar_archivos(carpeta):
    lista_archivos = []
    for ruta_actual, _, archivos in os.walk(carpeta):
        for archivo in archivos:
            ruta_completa = os.path.join(ruta_actual, archivo)
            lista_archivos.append(ruta_completa)
    return lista_archivos
print("Oprime Ctrl + C para salir en cualquier momento.")
print("----------------------------------------------------------------------------")
print(f"        Bienvenido al programa * UAM springerDataClimateMX *")
print("----------------------------------------------------------------------------")
print("Elige una Opcion")
print("Opcion 1: Crear el esquema de la base de datos climatologia_diaria")
print("Opcion 2: Ir al Programa DataMiner de la UAM CUAJIMALPA ")
opcion=input("Ingresa tu opción: ")
if opcion=="1":
    with open("CreaBDyOrg.py", 'r') as archivopy:
        contenido_script = archivopy.read()
        # Ejecutar el contenido del script
        exec(contenido_script)
        archivopy.close()
if opcion == "2":
    with open("main.py", 'r') as archivopy:
        contenido_script = archivopy.read()
        # Ejecutar el contenido del script
        exec(contenido_script)
        archivopy.close()
