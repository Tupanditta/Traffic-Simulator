"""
Definir la fecha exacta del inicio de la simulación

Establecer un clima inicial por defecto para el día 0, de ahí calculará el motor 
climático el temporal del día uno

Inicializar la estructura vacía donde iremos recopilando la información

Nombrar las variables iniciales que necesito. Es mejor hacerlo en una función aparte, así el cuerpo base
no tiene que entrar en el diccionario  en ningún momento
"""
import datetime
from .initial_state_statistical_functions import initial_weather

def variables(initial_state_dict: dict) -> tuple[datetime.date, dict, datetime.date]:
  """
  Del initial_state_dict solo necesito unos valores, estos los asigno a unas variables
  """
  yesterday_date_dict = initial_state_dict.copy()
  yesterday_date = yesterday_date_dict["date"]["date"]
  final_date = initial_state_dict["final_date"]

  return yesterday_date, yesterday_date_dict, final_date

def variable_yesterday_date(actual_date_dict: dict) -> datetime.date:
  """
  Devuelve la fecha del día de hoy
  """
  yesterday_date = actual_date_dict["date"]["date"]
  return yesterday_date

def create_initial_state(context_dict: dict) -> tuple[dict, list]:
  """
  Usa los datos contenidos en el context_dict para calcular los parámetros
  iniciales del día 0 (un día que no cuenta para la simulación)
  """
  dict_list = [] # los diccionarios de cada día se guardarán en una lista

  initial_state_dict = {
    "date": {
      "date": None,
      "day_type": None,
      "season": None
    }, 
    "final_date": None, 
    "weather": None, 
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
  } #Los diccionarios de cada día tendrán esta forma

  season = context_dict["season"] 
  initial_state_dict["date"]["season"] = season

  first_weather = initial_weather(context_dict)
  initial_state_dict["weather"] = first_weather

  one_day_less = datetime.timedelta(days=1) 
  first_date = datetime.date.fromisoformat(context_dict["seasons_dates"][season]["start"]) - one_day_less
  initial_state_dict["date"]["date"] =  first_date
  initial_state_dict["date"]["day_type"] = first_date.weekday()

  last_date = context_dict["seasons_dates"][season]["end"]
  initial_state_dict["final_date"] = datetime.date.fromisoformat(last_date)

  return initial_state_dict, dict_list