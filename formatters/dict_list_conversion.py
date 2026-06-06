"""
Antes de pasar todos los datos a la base de datos de SQL, hay que midificar varios datos que 
aparecen como integers para poder hacer los cálculos pero que su verdadero valor es una
cadena de texto

En este módulo se modifican los datos del actual_date_dict
"""

def dict_list_str_conversion(dict_list: list) -> list:
  """
  Itera sobre los diccionarios de cada día y en cada 
  iteración realiza la conversión, igual en todos los
  diccionarios de todos los días
  """
  #calculo los parámetros para las claves necesarias
  attribute_str_options = {0: "monday", 1: "tuesday", 2: "wednesday", 3: "thursday", 4: "friday", 5: "saturday", 6: "sunday"}
  season_str_options = {1: "winter", 2: "spring", 3: "summer", 4: "autumn"}

  #Tengo que cambiarlo en todos los diccionarios, por lo que tengo que recorrer la lista de diccionarios
  for dictionary in dict_list:
    #Lo puedo hacer ya que listas y diccionarios son mutables
    dictionary["date"]["attribute"] = attribute_str_options[dictionary["date"]["attribute"]]
    dictionary["date"]["season"] = season_str_options[dictionary["date"]["season"]]

  return dict_list