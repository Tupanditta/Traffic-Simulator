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

def read_statistical_data() -> dict:
  """
  Función de leer el archivo.json y pasar sus datos a un diccionario
  """
  print("Iniciando la lectura del archivo json con los Datos Estadísticos: ")

  # Construimos la ruta dinámica al JSON (busca en la misma carpeta que este script)
  actual_directory = os.path.dirname(__file__) #para saber cual es el directorio actual
  file_path = os.path.join(actual_directory, "statistical_data.json")

  try:
    with open(file_path, "r") as file:
      statistical_data_dict = json.load(file)
      print("Se han cargado los datos exitosamente")
      
      #El json no permite claves de valor int, por lo que se han escrito como str y ahora hay que 
      #convertirlos en integers
      statistical_data_dict = convert_all_keys(statistical_data_dict)

      #NOTA: no hace falta cerrar el archivo.json pues with open() ya lo hace por si solo

      return statistical_data_dict
    
  except FileNotFoundError as error_detail: 
    print(f"No se encontró el archivo {file_path}")
    print(f"El error se ubica en {error_detail}")
    sys.exit(1)
  except json.JSONDecodeError as error_detail:
    print(f"El archivo {file_path} está corrupto o mal formateado")
    print(f"Detalle técnico del error {error_detail}")
    sys.exit(1)

def convert_keys(key: str, statistical_data_dict: dict):
  """
  Convierte las claves de un subdiccionario a integers
  """
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

def convert_all_keys(statistical_data_dict: dict) -> dict:
  """
  Convierte todas las claves que están en str y que deberían de estar como integers
  """
  statistical_data_dict["transition_matrix"] = convert_keys("transition_matrix", statistical_data_dict)
      
  statistical_data_dict["environmental_multipliers"] = convert_keys("environmental_multipliers", statistical_data_dict)
  
  statistical_data_dict["seasons_dates"] = convert_keys("seasons_dates", statistical_data_dict)

  statistical_data_dict["initial_weather"] = convert_keys("initial_weather", statistical_data_dict)

  return statistical_data_dict