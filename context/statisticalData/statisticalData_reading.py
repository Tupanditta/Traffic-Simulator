"""
Este archivo se encarga de leer todos los datos estadísticos almacenados en el archivo json
Se hace así pues si se deben modificar los datos, añadir o borrar, lo que se modifica es el 
archivo json, no un archivo.py. De tal manera que el error ocurre fuera del flujo del proyecto
Es una forma de aislar lo que es el código de lo que es texto
Una vez ejecutado, si se lee el archivo.json correctamente, se devuelve un diccionario con toda
la información
Si hubiera algún error, el programa se detendrá y devolverá un mensaje de error. 
"""

import json
import sys
import os

def read_statistical_data():
  print("Iniciando la lectura del archivo json con los Datos Estadísticos: ")

  # Construimos la ruta dinámica al JSON (busca en la misma carpeta que este script)
  actual_directory = os.path.dirname(__file__)
  file_path = os.path.join(actual_directory, "statisticalData.json")

  try:
    with open(file_path, "r") as file:
      statistical_data_dict = json.load(file)
      print("Se han cargado los datos exitosamente")
        
      statistical_data_dict["transition_matrix"] = convert("transition_matrix", statistical_data_dict)
      
      statistical_data_dict["environmental_multipliers"] = convert("environmental_multipliers", statistical_data_dict)
      
      statistical_data_dict["seasons_dates"] = convert("seasons_dates", statistical_data_dict)

      statistical_data_dict["initial_weather"] = convert("initial_weather", statistical_data_dict)

      return statistical_data_dict
    
  except FileNotFoundError as error_detail: 
    print(f"No se encontró el archivo {file_path}")
    print(f"El error se ubica en {error_detail}")
    sys.exit(1)
  except json.JSONDecodeError as error_detail:
    print(f"El archivo {file_path} está corrupto o mal formateado")
    print(f"Detalle técnico del error {error_detail}")
    sys.exit(1)

def convert(key, statistical_data_dict):
  if key in statistical_data_dict:
    # Creamos un nuevo diccionario con las claves como int
    raw_matrix = statistical_data_dict[key]
    
    # Convertimos solo las claves del nivel 1 (1, 2, 3, 4)
    # Nota: Esto no afecta a "posible_states"
    clean_matrix = {}
    for k, v in raw_matrix.items():
      if k.isdigit(): # Comprobamos si es un número antes de convertir
        clean_matrix[int(k)] = v
      else:
        clean_matrix[k] = v # Mantenemos las listas de texto tal cual
    
    return clean_matrix
  
  return statistical_data_dict