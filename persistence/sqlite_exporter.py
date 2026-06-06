"""
Contiene las funciones necesarias para realizar la exportación de los datos
de las dict_list a la base de datos de sql, el archivo.db

Para ello es necesario crar la base de datos y antes de ello normalizar el diccionario
"""

import pandas as pd
import sqlite3 
import os

def export_to_sqlite(dict_list: list, output_folder: str):
  """
  Dirigir la exportación a sqlite
  """
  #Creo el nombre de la base de datos
  db_name = "traffic_accident_simulator(2).db"
  db_path = os.path.join(output_folder, db_name)

  #Creo el nombre de la tabla
  dict_list_tb_name = "daily_datas"

  #Normalizo los diccionarios
  dict_list_data_frame = normalize_datas(dict_list)

  create_data_base(dict_list_data_frame, db_path, dict_list_tb_name)

def normalize_datas(dict_list) -> list[dict]:
  """
  Normalizar los datos para después exportarlos
  """
  df_normalized = pd.json_normalize(dict_list, sep="_")
  return df_normalized

def create_data_base(dict_list_data_frame: pd.DataFrame, db_path: str, tb_name: str):
  """
  Es la que realiza la exporación
  """
  # 1. Crear el nombre del archivo de la base de datos
  print(f"\n[Persistencia] Abriendo conexión con la base de datos: {db_path}...")

  # 2. Abrir la conexión (Esto creará el archivo automáticamente en tu carpeta)
  conexion = sqlite3.connect(db_path)
  try:
    # 3. La inyección de datos
    dict_list_data_frame.to_sql(
      name=tb_name,             # El nombre de la tabla dentro de la base de datos
      con=conexion,             # Le pasamos el puente de conexión
      if_exists="append",       # Si la tabla existe, añade los datos al final
      index=False               # No queremos guardar la columna de números (0, 1, 2...)
    )
    print("¡Éxito! Los datos se han guardado correctamente en la base de datos.")

  except Exception as error_detail:
    # Si algo falla en SQL, nos avisará sin romper el programa entero
    print(f"[ERROR] Fallo al guardar en la base de datos: {error_detail}")
  
  finally:
    # 4. El cierre (Esta línea se ejecuta SIEMPRE, haya error o no)
    conexion.close()
    print("Conexión cerrada de forma segura.")