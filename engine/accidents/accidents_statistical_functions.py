"""
Contiene las funciones que calculan los accidentes

Estas funciones solo reciben parámetros numéricos, en ningun momento deben conocer
listas o diccionarios
"""

def calculate_risk_factor_multiplier(alcohol_percent: float, drugs_percent: float, alcohol_weight: float, drugs_weight: float, sober_weight: float):
  """
  Devuelve un multiplicador en base a los factores de riesgo
  """
  alcohol_percent = float(alcohol_percent)
  drugs_percent = float(drugs_percent)
  sober_percent = 100 - alcohol_percent - drugs_percent

  behavioral_multiplier_sum = (alcohol_percent*alcohol_weight) + (drugs_percent*drugs_weight) + (sober_percent*sober_weight)
  behavioral_multiplier = behavioral_multiplier_sum / 100

  return behavioral_multiplier


def calculate_group_accidents(traffic: int, base_accident_rate: float, weather_multiplier: float, behavioral_multiplier: float) -> int:
  """
  Calcula los accidentes de un grupo de edad
  """
  group_accidents = int(traffic) * base_accident_rate * weather_multiplier * behavioral_multiplier
  return int(group_accidents)