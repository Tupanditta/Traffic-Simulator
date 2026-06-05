import random

def initial_weather(context_dict): 
  # Declaro y doy valor a las variables que voy a necesitar
  season = context_dict["temporality"]

  # Busco en la matriz, la lista de probabilidades atribuidas a la estación
  initial_weather_dict = context_dict["initial_weather"][season]

  weather_list = context_dict["initial_weather"]["weather_list"] # Obtengo la lista de los posibles estados del weather
  probabilities_list = [initial_weather_dict[state] for state in weather_list] # De dicho diccionario solo quiero los valores floats

  first_weather = random.choices(
    population = weather_list,
    weights = probabilities_list,
  )

  first_weather = first_weather[0] # Paso de la lista que me devuelve random.choices a un string

  return first_weather