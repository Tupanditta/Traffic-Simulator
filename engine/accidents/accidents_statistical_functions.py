"""
Contiene las funciones que calculan los accidentes

Estas funciones solono se meten en diccionarios, ni en sus claves ni en sus valores
"""
import numpy as np
def calculate_risk_factor_multiplier(risk_factors_list: list, sober_list: list):
  """
  Devuelve un multiplicador en base a los factores de riesgo
  """
  behavioral_multiplier_sum = 0.0
  total_pct_sum = 0.0

  for pct, weight, group_mult in risk_factors_list:
    behavioral_multiplier_sum += pct*weight*group_mult
    total_pct_sum += pct
  
  sober_pct = 1 - total_pct_sum
  behavioral_multiplier_sum += sober_pct*sober_list[0]*sober_list[1]

  behavioral_multiplier = behavioral_multiplier_sum
  return behavioral_multiplier

def calculate_group_lambda(traffic: int, base_accident_rate: float, weather_multiplier: float, behavioral_multiplier: float) -> float:
  """
  Calcula el valor de lambda
  """
  group_lambda = traffic * base_accident_rate * weather_multiplier * behavioral_multiplier
  return group_lambda

def calculate_group_accidents(traffic: int, base_accident_rate: float, weather_multiplier: float, sober_list: list, risk_factors_list: list):
  """
  Calculo lambda y aplico la funció de poisson
  """

  behavioral_multiplier = calculate_risk_factor_multiplier(risk_factors_list, sober_list)
  lambda_value = calculate_group_lambda(traffic, base_accident_rate, weather_multiplier, behavioral_multiplier)
  
  group_accidents = np.random.poisson(lambda_value)
  
  return group_accidents