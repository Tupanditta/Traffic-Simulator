"""
Este módulo se encarga de validar los datos que introduce el usuario por pantalla

No importa ningún otro módulo, y por ahora solo se importa en reading.py

Cuidado puesto que las funciones dependen de que el parámetro de entrada sea el adecuado,
punto crítico del módulo reading. 
Por lo que un pequeño cambio en el reading.py puede afectar a este módulo
"""

def validate_temporality(temporality: int) -> bool:
  """
  Este solo valida si el valor int está en el intervalo
  """
  valid_values = pass_temporality_options()
  return temporality in valid_values

def pass_temporality_options() -> dict:
  """
  Defino las opciones que puede tomar el valor conceptual de temporality
  El diccionario se define en este módulo
  """
  temporality_options_dict = {
    1: "INVIERNO",
    2: "PRIMAVERA",
    3: "VERANO",
    4: "OTOÑO"
  }
  return temporality_options_dict

def validate_population(population: int) -> bool:
  """
  Exige que la población sea positiva, y un valor integer
  """
  return population > 0

def validate_risk_factors(risk_factor_percent: float) -> bool:
  """
  Comprueba si el valor introducido es un porcentaje
  """
  return 0 <= risk_factor_percent <= 100

def validate_demography(demography_percent: float, parcial_percents_sum: float) -> bool:
  """
  Devuelve un booleano que indica si el porcentaje es positivo
  Y si la suma parcial de todos los porcentajes está por debajo
  del 100%
  """
  return demography_percent >= 0 and 100 >= parcial_percents_sum + demography_percent

def pass_year_options() -> list:
  """
  Determina que años hay disponibles, y los pasa
  """
  year_options = [2017]
  return year_options

def validate_year(year: int) -> bool:
  """
  Solo comprueba si el año está en la lista
  """
  year_options = pass_year_options()
  return year in year_options