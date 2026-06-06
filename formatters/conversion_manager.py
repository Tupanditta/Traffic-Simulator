"""
Quien dirige todas las conversiones, recibe los diccionarios como parámetros, 
y usa las funciones para realizar la conversión. 

Pero como tal este no sabe como se hace la conversión ni que es eso, 
al igual que no sabe dentro de los diccionarios que hay ya que no se 
mete dentro

Este es simplemente el puente entre el main y las funciones de conversión
"""

from formatters.context_dict_conversion import context_dict_str_conversion
from formatters.dict_list_conversion import dict_list_str_conversion

def execute_conversion(dict_list: list, context_dict: dict) -> tuple[list, dict]:
  """
  Orquestador de las funciones, las llama y estas hacen la conversión
  """
  converted_dict_list = dict_list_str_conversion(dict_list)
  converted_context_dict = context_dict_str_conversion(context_dict)

  return converted_dict_list, converted_context_dict