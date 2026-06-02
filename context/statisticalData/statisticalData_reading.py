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
import os

def read_statisticalDatas():
  print("Iniciando la lectura del archivo json con los Datos Estadísticos: ")

  # Construimos la ruta dinámica al JSON (busca en la misma carpeta que este script)
  actual_directory = os.path.dirname(__file__)
  file_path = os.path.join(actual_directory, "statisticalData.json")

  try:
    with open(file_path, "r") as file:
      statisticalDatas = json.load(file)
      print("Se han cargado los datos exitosamente")

      if "Transition_Matrix" in statisticalDatas:
        # Creamos un nuevo diccionario con las claves como int
        raw_matrix = statisticalDatas["Transition_Matrix"]
        
        # Convertimos solo las claves del nivel 1 (1, 2, 3, 4)
        # Nota: Esto no afecta a "Posible_States"
        clean_matrix = {}
        for k, v in raw_matrix.items():
            if k.isdigit(): # Comprobamos si es un número antes de convertir
                clean_matrix[int(k)] = v
            else:
                clean_matrix[k] = v # Mantenemos "Posible_States" tal cual
        
        statisticalDatas["Transition_Matrix"] = clean_matrix
        
      return statisticalDatas
    
  except FileNotFoundError as errorDetail: 
    print(f"No se encontró el archivo {file_path}")
    print(f"El error se ubica en {errorDetail}")
    sys.exit(1)
  except json.JSONDecodeError as errorDetail:
    print(f"El archivo {file_path} está corrupto o mal formateado")
    print(f"Detalle técnico del error {errorDetail}")
    sys.exit(1)

