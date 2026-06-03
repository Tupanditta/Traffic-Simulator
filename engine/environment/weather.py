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

def create_weather(context_dict, actual_date_dict, yesterday_date_dict):
  # Declaro y doy valor a las variables que voy a necesitar
  season = actual_date_dict["date"]["season"]
  yesterday_weather = yesterday_date_dict["weather"]

  # Busco en la matriz, la lista de probabilidades atribuidas al clima de ayer
  transition_matrix = context_dict["transition_matrix"][season][yesterday_weather] 

  posible_states = context_dict["transition_matrix"]["posible_states"] # Obtengo la lista de los posibles estados
  probabilities_list = [transition_matrix[state] for state in posible_states] # De dicho diccionario solo quiero los valores floats

  new_weather = random.choices(
    population = posible_states,
    weights = probabilities_list,
  )

  new_weather = new_weather[0] # Paso de la lista que me devuelve random.choices a un string

  return new_weather

def update_weather(context_dict, actual_date_dict, yesterday_date_dict):
  new_weather = create_weather(context_dict, actual_date_dict, yesterday_date_dict)
  actual_date_dict["weather"] = new_weather
  
  return actual_date_dict