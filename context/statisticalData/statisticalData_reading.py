"""
Este archivo se encarga de leer todos los datos estadísticos almacenados en el archivo json
Se hace así pues si se deben modificar los datos, añadir o borrar, lo que se modifica es el 
archivo json, no un archivo.py. De tal manera que el error ocurre fuera del flujo del proyecto
Es una forma de aislar lo que es el código de lo que es texto
Una vez ejecutado, si se lee el archivo.json correctamente, se devuelve un diccionaro con toda
la información
Si hubiera algún error, el programa se detendrá y devolvera un mensaje de error. 
"""

import json
import sys

def read_statisticalDatas(file_path):
  print("Iniciando la lectura del archivo json con los Datos Estadísticos: ")

  try:
    with open(file_path, "r") as file:
      statisticalDatas = json.load(file)
      print("Se han cargado los datos exitosamente")
      return statisticalDatas
    
  except FileNotFoundError as errorDetail: 
    print(f"No se encontró el archivo {file_path}")
    print(f"El error se ubica en {errorDetail}")
    sys.exit(1)
  except json.JSONDecodeError as errorDetail:
    print(f"El archivo {file_path} está corrupto o mal formateado")
    print(f"Detalle técnico del error {errorDetail}")
    sys.exit(1)

statiscalDatas = read_statisticalDatas(r"C:\Users\ander\Desktop\Kirby\Python\py\mis_funciones\TrafficAccidentSimulator\code\context\statisticalData\statisticaData.json")
print(statiscalDatas)