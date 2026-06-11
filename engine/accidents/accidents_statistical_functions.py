"""
Contiene las funciones que calculan los accidentes

Estas funciones solono se meten en diccionarios, ni en sus claves ni en sus valores
"""
import numpy as np
import itertools
import math

def calculate_risk_factor_multiplier(risk_factors_list: list):
  """
  Devuelve un multiplicador en base a los factores de riesgo
  """
  behavioral_multiplier_sum = 0.0
  total_pct_sum = 0.0

  itertools_list = build_itertools_list(risk_factors_list)

  combinations = list(itertools.product(*itertools_list))

  for combination in combinations:
    probabilities = [state[0] for state in combination]
    values = [state[1] for state in combination]

    state_probability = math.prod(probabilities)
    state_value = math.prod(values)

    behavioral_multiplier_sum += state_probability*state_value
    total_pct_sum += state_probability

  behavioral_multiplier = behavioral_multiplier_sum
  return behavioral_multiplier

def calculate_group_lambda(traffic: int, base_accident_rate: float, weather_multiplier: float, behavioral_multiplier: float) -> float:
  """
  Calcula el valor de lambda
  """
  group_lambda = traffic * base_accident_rate * weather_multiplier * behavioral_multiplier
  return group_lambda

def calculate_group_accidents(traffic: int, base_accident_rate: float, weather_multiplier: float, risk_factors_list: list):
  """
  Calculo lambda y aplico la función de poisson
  para calcular el total de accidentes
  """

  behavioral_multiplier = calculate_risk_factor_multiplier(risk_factors_list)
  lambda_value = calculate_group_lambda(traffic, base_accident_rate, weather_multiplier, behavioral_multiplier)
  
  group_accidents = np.random.poisson(lambda_value)
  
  return group_accidents

def calculate_effective_risk_pct(actual_pct, relative_pct):
  """
  Al inicio, el usuario introduce que porcentaje del grupo de edad consume cada factor de riesgo
  No obstante, de todo ese porcentaje no todos consumen dicho factor a la hora de conducir
  Esta fórmula calcula el porcentaje absoluto, basandose en un porcentaje relativo del json
  """
  return actual_pct * relative_pct

def build_itertools_list(risk_factors_list):
  itertools_list = [] #Lista de sublista por cada factor

  for pct, weight, group_mult in risk_factors_list:
    itertools_sublist = []

    itertools_sublist.append((1-pct, 1.0)) #Estado en el que el factor de riesgo no se da
    itertools_sublist.append((pct, weight*group_mult)) #Estado en el que el factor de riesgo sí se da
    
    itertools_list.append(itertools_sublist)
  
  return itertools_list