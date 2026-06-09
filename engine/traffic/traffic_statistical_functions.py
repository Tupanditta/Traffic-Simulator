"""
Contiene las fórmulas necesarias para calcular el tráfico

Estas fórmulas no sabe de la existencia de diccionarios, solo 
recibe parámetros numéricos y hace el cálculo
"""

import math
import random

def calculate_group_traffic_average(average_base: float, volume_multipliers_list: list) -> float:
  """
  Calcula el tráfico medio de cada grupo demográfico
  """
  total_multiplier = math.prod(volume_multipliers_list)
  group_traffic_average = average_base * total_multiplier

  return group_traffic_average

def calculate_group_traffic_standart_deviation(average: float, standart_deviation_base: float, standart_deviation_sum_list: list):
  total_group_traffic_standart_deviation = standart_deviation_base + sum(standart_deviation_sum_list)
  return total_group_traffic_standart_deviation * average

def calculate_group_traffic(average_base: float, standart_deviation_base: float, volume_multipliers_list: list, standart_deviation_sum_list: list) -> int:
  group_traffic_average_value = calculate_group_traffic_average(average_base, volume_multipliers_list)
  group_traffic_standart_deviation_value = calculate_group_traffic_standart_deviation(group_traffic_average_value, standart_deviation_base, standart_deviation_sum_list)

  group_traffic = max(0, int(random.gauss(group_traffic_average_value, group_traffic_standart_deviation_value)))

  return group_traffic