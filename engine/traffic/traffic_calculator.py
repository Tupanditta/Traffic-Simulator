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
  season = actual_date_dict["date"]["season"] #Común para todo

  today_conditions_dict = {
    "weather": actual_date_dict["weather"],
    "day_type": convert_day_type(actual_date_dict["date"]["day_type"])
  }

  demography_groups_dict: dict = context_dict["demography"] #Lista de los diferentes grupos de edad

  total_traffic = 0 #Inicializo la suma parcial a 0

  for group in demography_groups_dict.keys(): #calculo el tráfico por grupo y hago la suma parcial

    #Parámetros para la función estadística (son necesarios)
      #Parámetros base
    average_base = context_dict["groups_base_exposure_rate"][group] * population * context_dict["demography"][group]
    standart_deviation_base = context_dict["groups_base_volatility_rate"][group]

      #Parámetros listas
    volume_multipliers_list, standart_deviation_sum_list = create_parameters_list(context_dict, season, today_conditions_dict)

    #Llamo a la función que hace el cálculo
    group_traffic = calculate_group_traffic(average_base, standart_deviation_base, volume_multipliers_list, standart_deviation_sum_list)

    #Introduzco el valor del tráfico en su respectivo lugar en el diccionario del día de hoy
    actual_date_dict["traffic"][group] = int(group_traffic)

    #Voy actualizando el tráfico total
    total_traffic += int(group_traffic)

  #Introduzco el valor del tráfico total en el diccionario del día de hoy
  actual_date_dict["traffic"]["total"] = total_traffic

  return actual_date_dict

def convert_day_type(day_type: int) -> str:
  """
  Le paso el día de la semana 0-6, y me devuelve si es laborable o finde
  """
  weekend_list = [5, 6]
  workday_list = [0, 1, 2, 3, 4]
  if day_type in weekend_list: return "weekend"
  if day_type in workday_list: return "workday"

def create_parameters_list(context_dict: dict, season: int, today_conditions_dict: dict):
  volume_multipliers_list = []
  standart_deviation_sum_list = []

  for modifier_name, modifier_value in today_conditions_dict.items():
    volume_multiplier = context_dict["traffic_modifiers"]["volume_multipliers"][modifier_name][season][modifier_value]
    chaos_modifier = context_dict["traffic_modifiers"]["chaos_modifiers"][modifier_name][season][modifier_value]

    volume_multipliers_list.append(volume_multiplier)
    standart_deviation_sum_list.append(chaos_modifier)

  return volume_multipliers_list, standart_deviation_sum_list