"""
Definir la fecha exacta del inicio de la simulación

Establecer un clima inicial por defecto para el día 0, de ahí calculará el motor 
climático el temporal del día uno

Inicializar la estructura vacía donde iremos recopilando la información

Nombrar las variables iniciales que necesito. Es mejor hacerlo en una función aparte, así el cuerpo base
no tiene que entrar en el diccionario
"""
import datetime

def variables(initial_state_dict):
  yesterday_date_dict = initial_state_dict
  yesterday_date = yesterday_date_dict["date"]["date"]
  final_date = initial_state_dict["final_date"]

  return yesterday_date, yesterday_date_dict, final_date

def create_initial_state(context_dict):
  dict_list = [] # los diccionarios de cada día se guardarán en una lista
  initial_state_dict = {
    "date": {
      "date": datetime.date(2017, 12, 10),
      "attribute": datetime.date(2017, 12, 10).weekday(),
      "season": 2
    }, 
    "final_date": datetime.date(2017, 12, 13), # hay que cambiarlo, me lo he inventado
    "weather": "rain", 
    "traffic": {
      "total": None,
      "children": None,
      "teenagers": None,
      "adults": None,
      "olders": None
    }, 
    "accidents": {
      "children": None,
      "teenagers": None, 
      "adults": None, 
      "olders": None,
      "total": None
    }
  }
  return initial_state_dict, dict_list