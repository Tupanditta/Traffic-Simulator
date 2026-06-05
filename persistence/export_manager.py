import os

from persistence.sqlite_exporter import export_to_sqlite
from persistence.json_exporter import export_to_json

def get_output_directory():
    """
    Calcula dinámicamente la ruta para crear una carpeta 'outputs' 
    fuera de la carpeta de código fuente.
    """
    # 1. Obtenemos la ruta absoluta de este script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Subimos los niveles necesarios (Ajusta los ".." según tus carpetas)
    root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
    
    # 3. Definimos la carpeta de destino
    outputs_dir = os.path.join(root_dir, "outputs")
    
    # 4. Creamos la carpeta (exist_ok=True evita errores si ya estaba creada)
    os.makedirs(outputs_dir, exist_ok=True)
    
    return outputs_dir

def execute_exports(dict_list, context_dict):
    """
    Función principal a la que llamará el bucle de tu simulador al terminar.
    """   
    # 1. Obtención de la carpeta de salida
    output_folder = get_output_directory()

    # 2. Ejecución de las exportaciones modulares
    export_to_json(context_dict, output_folder)
    export_to_sqlite(dict_list, output_folder)
    
    print("\n=== FASE DE PERSISTENCIA COMPLETADA ===")