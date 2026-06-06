"""
Un archivo con funciones que lo que harán es calcular el clima, 
no le interesa ese clima como va a repercutir en el resto del código

Este se basa tanto en las estructuras de datos que lee statisticalData_reading.py
como en las operaciones necesarias para calcular las probabilidades de cada estado 
del clima y así elegir un estado para cada día

Devuelve ya el diccionario con el nuevo valor del weather, así el bucle principal
no tiene que acceder al diccionario en ningún momento
"""

import random

def create_weather(context_dict: dict, actual_date_dict: dict, yesterday_date_dict: dict) -> str:
  """
  Calculo el nuevo weather para el día actual
  """
  # Declaro y doy valor a las variables que voy a necesitar
  season = actual_date_dict["date"]["season"]
  yesterday_weather = yesterday_date_dict["weather"]

  # Busco en la matriz, la lista de probabilidades atribuidas al clima de ayer
  transition_matrix = context_dict["transition_matrix"][season][yesterday_weather] 

  weather_list = context_dict["transition_matrix"]["weather_list"] # Obtengo la lista de los posibles estados del weather
  probabilities_list = [transition_matrix[state] for state in weather_list] # De dicho diccionario solo quiero los valores floats

  new_weather = random.choices(
    population = weather_list,
    weights = probabilities_list,
  )

  new_weather = new_weather[0] # Paso de la lista que me devuelve random.choices a un string

  return new_weather

def update_weather(context_dict: dict, actual_date_dict: dict, yesterday_date_dict: dict) -> dict:
  """
  Llamo a la fución que calcula el nuevo weather y lo introduzco en el diccionario
  del día actual
  """
  new_weather = create_weather(context_dict, actual_date_dict, yesterday_date_dict)
  actual_date_dict["weather"] = new_weather
  
  return actual_date_dict