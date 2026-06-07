"""
Calcula los accidentes totales y de cada grupo y actualiza el diccionario del día

Se basa en unas fórmulas estadísticas del módulo statistical_functions

De quienes calculan los accidentes, solo este módulo se mete dentro de diccionarios, ninguno más
"""

from .accidents_statistical_functions import calculate_group_accidents
from typing import TypedDict

def calculate_accidents(actual_date_dict: dict, context_dict: dict) -> dict:
  """
  Calcula y actualiza los datos de los accidentes totales y de cada 
  grupo de edad
  """
  # Extraigo los datos generales que aplican a todos los grupos
  weather = actual_date_dict["weather"]
  season = actual_date_dict["date"]["season"]
  base_accident_rate = context_dict["base_accident_rate"]
  
  # Extraigo los pesos fijos del comportamiento
  distractions_elec_div_weight = context_dict["behavioral_multipliers"]["distractions_elec_div"]
  alcohol_weight = context_dict["behavioral_multipliers"]["alcohol"]
  drugs_weight = context_dict["behavioral_multipliers"]["drugs"]
  sober_weight = context_dict["behavioral_multipliers"]["sober"]

  total_accidents = 0

  #Variables y diccionarios necesarios para el bucle
  demography_dict: dict = context_dict["demography"]
  demography_groups = demography_dict.keys()

  # Bucle por cada grupo de edad
  for group in demography_groups:
    
    #Factores de riesgo DICCIONARIOS
    alcohol_dict: dict = context_dict["risk_factors"]["alcohol"]
    drugs_dict: dict = context_dict["risk_factors"]["drugs"]
    distractions_elec_div_dict: dict = context_dict["risk_factors"]["distractions_elec_div"]

    #Factores de riesgo PORCENTAJES
    alcohol_pct = alcohol_dict.get(group, 0.0)
    drugs_pct = drugs_dict.get(group, 0.0)
    distractions_elec_div_pct = distractions_elec_div_dict.get(group, 0.0)
    
    #Otros parámetros 
    weather_multiplier = context_dict["environmental_multipliers"][season][weather]
    group_traffic = actual_date_dict["traffic"][group]

    #Calcular los accidentes del grupo de edad
    group_accidents = calculate_group_accidents(group_traffic, base_accident_rate, weather_multiplier, alcohol_pct, drugs_pct, distractions_elec_div_pct, alcohol_weight, drugs_weight, distractions_elec_div_weight, sober_weight)

    #Actualizar variable total_accidents y el diccionario
    actual_date_dict["accidents"][group] = group_accidents
    total_accidents += group_accidents

  actual_date_dict["accidents"]["total"] = total_accidents
  
  return actual_date_dict

