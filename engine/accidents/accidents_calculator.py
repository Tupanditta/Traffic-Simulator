"""
Calcula los accidentes totales y de cada grupo y actualiza el diccionario del día

Se basa en unas fórmulas estadísticas del módulo statistical_functions

De quienes calculan los accidentes, solo este módulo se mete dentro de diccionarios, ninguno más
"""

from .accidents_statistical_functions import calculate_group_accidents, calculate_effective_risk_pct
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

  total_accidents = 0

  #Variables y diccionarios necesarios para el bucle
  demography_dict: dict = context_dict["demography"]
  demography_groups = demography_dict.keys()

  # Bucle por cada grupo de edad
  for group in demography_groups:
    
    #Otros parámetros 
    weather_multiplier = context_dict["environmental_multipliers"][season][weather]
    group_traffic = actual_date_dict["traffic"][group]
    
    risk_factors_list = build_risk_factors_list(context_dict, group) #Creo la lista específica para cada grupo de edad

    #Calcular los accidentes del grupo de edad
    group_accidents = calculate_group_accidents(group_traffic, base_accident_rate, weather_multiplier, risk_factors_list)

    #Actualizar variable total_accidents y el diccionario
    actual_date_dict["accidents"][group] = group_accidents
    total_accidents += group_accidents

  actual_date_dict["accidents"]["total"] = total_accidents
  
  return actual_date_dict

def build_risk_factors_list(context_dict: dict, group: str):
  """
  Se crea la lista de parámetros que se le pasará a la calculadora de accidentes
  Consiste en grupos de 3 datos, el pct del facor de riesgo, el peso que tiene probabilísticamente
  y un multiplicador por el grupo de edad
  """
  risk_factors_list = []
  effective_risk_pct_dict = context_dict["effective_risk_percentage"] #Para ahorrar líneas de código

  for risk_factor_name, risk_factor_dict in context_dict["risk_factors"].items():
    risk_factor_pct = calculate_effective_risk_pct(risk_factor_dict.get(group, 0.0), effective_risk_pct_dict[risk_factor_name][group])
    risk_factor_weight = context_dict["behavioral_multipliers"][risk_factor_name]["weight"]
    group_multiplier = context_dict["behavioral_multipliers"][risk_factor_name]["group_multiplier"][group]

    risk_factors_list.append((risk_factor_pct, risk_factor_weight, group_multiplier)) #Se añaden grupos de 3 elementos para cada factor de riesgo

  return risk_factors_list