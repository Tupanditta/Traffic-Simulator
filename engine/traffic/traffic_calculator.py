"""
Se encarga de calcular el tráfico total tanto el de cada grupo demográfico

Usa una fórmula, la cual puede ir cambiando con el tiempo dependiendo de si se añaden 
factores o datos que influyan en algún aspecto del tráfico
"""

from .traffic_statistical_functions import calculate_group_traffic

def calculate_traffic(actual_date_dict: dict, context_dict: dict) -> dict:
  """
  Esta función dirige el cálculo del tráfico, y recopila los datos necesarios para ello
  """
  #Defino las variables que voy a necesitar
  population = context_dict["population"]
  weather = actual_date_dict["weather"]
  attribute = convert_attribute(actual_date_dict["date"]["attribute"]) #es weekend o workday?

  demography_groups_dict: dict = context_dict["demography"] #Lista de los diferentes grupos de edad

  #Obtengo los diccionarios que contienen los datos estadísticos necesarios para el cálculo
  traffic_exposure_percentages_dict: dict = context_dict["traffic_exposure_percentages"]
  weather_traffic_multipliers_dict: dict = context_dict["weather_traffic_multipliers"]

  total_traffic = 0 #Inicializo la suma parcial a 0

  for group in demography_groups_dict.keys(): #calculo el tráfico por grupo y hago la suma parcial
    #parámetros para la función estadística
    demography_percent = demography_groups_dict[group]
    weather_multiplier = weather_traffic_multipliers_dict[group][weather]
    traffic_exposure_percentage = traffic_exposure_percentages_dict[group][attribute]

    #Llamo a la función que hace el cálculo
    group_traffic = calculate_group_traffic(population, demography_percent, weather_multiplier, traffic_exposure_percentage)
    
    #Introduzco el valor del tráfico en su respectivo lugar en el diccionario del día de hoy
    actual_date_dict["traffic"][group] = int(group_traffic)

    #Voy actualizando el tráfico total
    total_traffic += int(group_traffic)

  #Introduzco el valor del tráfico total en el diccionario del día de hoy
  actual_date_dict["traffic"]["total"] = total_traffic

  return actual_date_dict

def convert_attribute(attribute: int) -> str:
  """
  Le paso el día de la semana 0-6, y me devuelve si es laborable o finde
  """
  weekend_list = [5, 6]
  workday_list = [0, 1, 2, 3, 4]
  if attribute in weekend_list: return "weekend"
  if attribute in workday_list: return "workday"