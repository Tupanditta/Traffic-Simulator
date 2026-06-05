"""
Antes de pasar todos los datos a la base de datos de SQL, hay que midificar varios datos que 
aparecen como integers para poder hacer los cálculos pero que su verdadero valor es una
cadena de texto

En este módulo se modifican los datos del context_dict
"""
from formatters.core_conversion import do

def context_dict_str_conversion(context_dict):
  """
  Los datos a convertir siempre tienen sus respectivos valores en una lista, ordenada
  """
  #calculo los parámetros para las claves necesarias
  posible_states_transition_matrix = context_dict["transition_matrix"]["seasons_list"]
  posible_states_environmental_multipliers = context_dict["environmental_multipliers"]["seasons_list"]
  posible_states_initial_weather = context_dict["initial_weather"]["seasons_list"]

  #Hago la llamada a la función de conversión y modifico el diccionario
  context_dict["transition_matrix"] = do(context_dict["transition_matrix"], posible_states_transition_matrix)
  context_dict["environmental_multipliers"] = do(context_dict["environmental_multipliers"], posible_states_environmental_multipliers)
  context_dict["initial_weather"] = do(context_dict["initial_weather"], posible_states_initial_weather)

  return context_dict

