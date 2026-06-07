"""
Contiene las funciones que calculan los accidentes

Estas funciones solo reciben parámetros numéricos, en ningun momento deben conocer
listas o diccionarios
"""
import numpy as np
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


def calculate_group_lambda(traffic: int, base_accident_rate: float, weather_multiplier: float, behavioral_multiplier: float) -> float:
  """
  Calcula el valor de lambda
  """
  group_lambda = traffic * base_accident_rate * weather_multiplier * behavioral_multiplier
  return group_lambda

def calculate_group_accidents(traffic: int, base_accident_rate: float, weather_multiplier: float, alcohol_pct: float, drugs_pct: float, distractions_elec_div_pct: float, alcohol_weight: float, drugs_weight: float, distractions_elec_div_weight: float, sober_weight: float):
  """
  Calculo lambda y aplico la funció de poisson
  """

  behavioral_multiplier = calculate_risk_factor_multiplier(alcohol_pct, drugs_pct, alcohol_weight, drugs_weight, sober_weight, distractions_elec_div_weight, distractions_elec_div_pct)
  lambda_value = calculate_group_lambda(traffic, base_accident_rate, weather_multiplier, behavioral_multiplier)
  
  group_accidents = np.random.poisson(lambda_value)
  
  return group_accidents