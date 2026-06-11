"""
Para la acción de exportar el contenido del context a un archivo.json

No se mete en el context como tal, por lo que si este está mal este módulo 
no hay que cambiar nada
"""

import os
import json

def export_to_json(context_dict: dict, output_folder: str):
    """
    Realiza la acción de exportar el contenido del context a un archivo.json
    """
    json_file_path = os.path.join(output_folder, "context_dict_export(version 2.1.0).json")
    print(f"\n[Persistencia] Exportando configuración JSON a: {json_file_path}...")
    
    try:
        with open(json_file_path, "w", encoding="utf-8") as file:
            # indent=4 garantiza que el JSON se despliegue de forma jerárquica y visual
            json.dump(context_dict, file, indent=4, ensure_ascii=False)
        print(" -> ¡Éxito! Archivo JSON guardado correctamente.")
        
    except TypeError as error_detail:
        print(" -> [ERROR] El diccionario contiene un tipo de dato incompatible con JSON.")
        print(f" -> Detalle: {error_detail}")
    except PermissionError:
        print(f" -> [ERROR] No hay permisos de escritura en la ruta: {json_file_path}")
    except Exception as error_detail:
        print(f" -> [ERROR CRÍTICO] Fallo inesperado al exportar el JSON: {error_detail}")