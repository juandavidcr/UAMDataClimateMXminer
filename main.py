#!/usr/bin/env python
# decoding: utf-8
# Script que separa la información de los txt
from functions.script1DataCleanUp import getInfoDataTable,getInfoData
from infoBD import buscar_archivos
from pexpect import EOF
# hayEstaciones=False
print("Oprime Ctrl + C para salir en cualquier momento.")
print("----------------------------------------------------------------------------")
print(f"        Bienvenido al programa * UAM springerDataClimateMX *")
print("----------------------------------------------------------------------------")
print(f'Instrucciones: 1.- Cargar archivos de estaciones climatologicas dentro de la carpeta ------------> bancdata.\n Por cada carpeta de municipio nombrada poner adentro los archivos de las estaciones pertinentes. Produciremos 2 archivos que contienen ciertos patrones de comportamiento y localización dentro de las fuentes tomadas de un kmz de la aplicacion de google earth del siguiente link: https://smn.conagua.gob.mx/tools/RESOURCES/estacion/EstacionesClimatologicas.kmz . \n')
print(f'2.- Crear la base de datos a partir del archivo bd/sql-queries/db.sql \n')
print("O corriendo el comando python3 CreaBDyOrg.py")
print(f'3.- Crear catalogos de Organismo,Municipio y Estados_Republica_Mex a partir del archivo bd/sql-queries/dumps/<fecha>.sql, se deben buscar las tablas en el dump. \n')
print("Ejemplo: ./bancdata")