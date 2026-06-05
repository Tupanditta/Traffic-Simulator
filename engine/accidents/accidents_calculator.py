"""
Calcula los accidentes totales y de cada grupo y actualiza el diccionario del día

Se basa en unas fórmulas estadísticas del módulo statistical_functions
"""

from .accidents_statistical_functions import calculate_risk_factor_multiplier, calculate_group_accidents
from typing import TypedDict

def calculate_accidents(actual_date_dict, context_dict: dict):
  # Extraigo los datos generales que aplican a todos los grupos
  weather = actual_date_dict["weather"]
  season = actual_date_dict["date"]["season"]
  base_rate = context_dict["base_accident_rate"]
  
  # Extraigo los pesos fijos del comportamiento
  alcohol_weight = context_dict["behavioral_multipliers"]["alcohol"]
  drugs_weight = context_dict["behavioral_multipliers"]["drugs"]
  sober_weight = context_dict["behavioral_multipliers"]["sober"]

  total_accidents = 0
  demography_dict: dict = context_dict["demography"]
  demography_groups = demography_dict.keys()

  # Bucle por cada grupo de edad
  for group in demography_groups:
      
    group_traffic = actual_date_dict["traffic"][group]
    
    alcohol_dict: dict = context_dict["risk_factors"]["alcohol"]
    drugs_dict: dict = context_dict["risk_factors"]["drugs"]
    alcohol_pct = alcohol_dict.get(group, 0.0)
    drugs_pct = drugs_dict.get(group, 0.0)
    
    env_multiplier = context_dict["environmental_multipliers"][season][weather]

    beh_multiplier = calculate_risk_factor_multiplier(alcohol_pct, drugs_pct, alcohol_weight, drugs_weight, sober_weight)
    group_accidents = calculate_group_accidents(group_traffic, base_rate, env_multiplier, beh_multiplier)

    actual_date_dict["accidents"][group] = group_accidents
    total_accidents += group_accidents

  actual_date_dict["accidents"]["total"] = total_accidents
  
  return actual_date_dict