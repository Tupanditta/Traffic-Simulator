"""
Contiene las funciones que calculan los accidentes

Estas funciones solo reciben parámetros numéricos, en ningun momento deben conocer
listas o diccionarios
"""

def calculate_risk_factor_multiplier(alcohol_pct: float, drugs_pct: float, alcohol_weight: float, drugs_weight: float, sober_weight: float, distractions_elec_div_weight: float, distractions_elec_div_pct: float):
  """
  Devuelve un multiplicador en base a los factores de riesgo
  """
  alcohol_pct = float(alcohol_pct)
  drugs_pct = float(drugs_pct)
  sober_pct = 100 - alcohol_pct - drugs_pct

  behavioral_multiplier_sum = (alcohol_pct*alcohol_weight) + (drugs_pct*drugs_weight) + (sober_pct*sober_weight) + (distractions_elec_div_pct*distractions_elec_div_weight)
  behavioral_multiplier = behavioral_multiplier_sum / 100

  return behavioral_multiplier


def calculate_group_accidents(traffic: int, base_accident_rate: float, weather_multiplier: float, behavioral_multiplier: float) -> int:
  """
  Calcula los accidentes de un grupo de edad
  """
  group_accidents = int(traffic) * base_accident_rate * weather_multiplier * behavioral_multiplier
  return int(group_accidents)