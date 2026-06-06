"""
El manager de las funciones de exportación

Calcula y crea la ruta a la que se van a exportar los dos archivos

Luego llama a las funciones de exporación
"""

import os

from persistence.sqlite_exporter import export_to_sqlite
from persistence.json_exporter import export_to_json

def get_output_directory() -> str:
    """
    Calcula dinámicamente la ruta para crear una carpeta 'outputs' 
    fuera de la carpeta de código fuente.
    """
    #Obtenemos la ruta absoluta de este script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    #Subimos los niveles necesarios (Ajusta los ".." según tus carpetas)
    root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
    
    #Definimos la carpeta de destino
    outputs_dir = os.path.join(root_dir, "outputs")
    
    #Creamos la carpeta (exist_ok=True evita errores si ya estaba creada)
    os.makedirs(outputs_dir, exist_ok=True)
    
    return outputs_dir

def execute_exports(dict_list: list, context_dict: dict):
    """
    Función principal a la que llamará el bucle de tu simulador al terminar.
    """   
    #Carpeta de salida
    output_folder = get_output_directory()
    
    #Llamar a las funciones
    export_to_json(context_dict, output_folder)
    export_to_sqlite(dict_list, output_folder)
    
    print("\n=== FASE DE PERSISTENCIA COMPLETADA ===")