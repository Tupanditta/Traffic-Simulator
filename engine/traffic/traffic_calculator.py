"""
Se encarga de calcular el tráfico total tanto el de cada grupo demográfico

Usa una fórmula, la cual puede ir cambiando con el tiempo dependiendo de si se añaden 
factores o datos que influyan en algún aspecto del tráfico
"""

from engine.statistical_functions import calculate_group_traffic

def calculate_traffic(actual_date_dict, context_dict):
  population = context_dict["population"]
  weather = actual_date_dict["weather"]
  attribute = convert_attribute(actual_date_dict["date"]["attribute"]) #es weekend o workday?

  demography_groups_dict: dict = context_dict["demography"]
  traffic_exposure_percentages_dict: dict = context_dict["traffic_exposure_percentages"]
  weather_traffic_multipliers_dict: dict = context_dict["weather_traffic_multipliers"]

  total_traffic = 0

  for group in demography_groups_dict.keys(): #calculo el tráfico por grupo y hago la suma parcial
    #parámetros para la función estadística
    demography_percent = demography_groups_dict[group]
    weather_multiplier = weather_traffic_multipliers_dict[group][weather]
    traffic_exposure_percentage = traffic_exposure_percentages_dict[group][attribute]

    group_traffic = calculate_group_traffic(population, demography_percent, weather_multiplier, traffic_exposure_percentage)
    
    actual_date_dict["traffic"][group] = int(group_traffic)
    total_traffic += int(group_traffic)

  actual_date_dict["traffic"]["total"] = total_traffic

  return actual_date_dict

def convert_attribute(attribute) -> str:
  """
  Le paso el día de la semana 0-6, y me devuelve si es laborable o finde
  """
  weekend_list = [5, 6]
  workday_list = [0, 1, 2, 3, 4]
  if attribute in weekend_list: return "weekend"
  if attribute in workday_list: return "workday"