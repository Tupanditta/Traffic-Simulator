"""
Este módulo se encarga de validar los datos que introduce el usuario por pantalla

No importa ningún otro módulo, y por ahora solo se importa en reding.py

Cuidado puesto que las funciones dependen de que el parámetro de entrada sea el adecuado,
punto crítico del módulo reading. 
Por lo que un pequeño cambio en el reading.py puede afectar a este módulo
"""

def validate_temporality(temporality) -> bool:
  """
  Este solo valida si el valor int está en el intervalo
  """
  valid_values = pass_temporality_options()
  return temporality in valid_values

def pass_temporality_options():
  """
  defino las opciones que puede tomar el valor conceptual de temporality
  el diccionario se define en este módulo
  """
  temporality_options_dict = {
    1: "VERANO",
    2: "INVIERNO",
    3: "OTOÑO",
    4: "PRIMAVERA"
  }
  return temporality_options_dict


def validate_population(population) -> bool:
  """
  por ahora solo voy a exigir que la población sea positiva
  luego si eso ya añadiré algo más
  """
  return population > 0 

def validate_riskFactors(riskFactor_percent) -> bool:
  return 0 <= riskFactor_percent <=100

def validate_demography(demography_percent, parcial_percents_sum) -> bool:
  return demography_percent >= 0 and 100 >= parcial_percents_sum+demography_percent