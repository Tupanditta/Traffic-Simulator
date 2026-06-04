import pandas as pd
import sqlite3 

def export_to_sqlite(dict_list):
  #Tengo que normalizar los diccionarios, aplanarlos
  df_normalized = normalize_datas(dict_list)

  # 1. Crear el nombre del archivo de la base de datos
  db_name = "simulador_accidentes.db"
  print(f"Abriendo conexión con la base de datos: {db_name}...")

  # 2. Abrir la conexión (Esto creará el archivo automáticamente en tu carpeta)
  conexion = sqlite3.connect(db_name)

  try:
      # 3. La inyección de datos
      df_normalized.to_sql(
          name="registros_diarios", # El nombre de la tabla dentro de la base de datos
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

def normalize_datas(dict_list):
  df_normalized = pd.json_normalize(dict_list, sep="_")
  return df_normalized