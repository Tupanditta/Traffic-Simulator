"""
Definir la fecha exacta del inicio de la simulación

Establecer un clima inicial por defecto para el día 0, de ahí calculará el motor 
climático el temporal del día uno

Inicializar la estructura vacía donde iremos recopilando la información

Nombrar las variables iniciales que necesito. Es mejor hacerlo en una función aparte, así el cuerpo base
no tiene que entrar en el diccionario
"""
import datetime

def variables(initialState_Dict):
  yesterday_date_dict = initialState_Dict
  yesterday_date = yesterday_date_dict["Date"]["Date"]
  final_date = initialState_Dict["Final Date"]

  return yesterday_date, yesterday_date_dict, final_date

def create_InitialState(context_dict):
  dictList = [] #los diccionarios de cada día se guardarán en un lista
  initialState_Dict = {
    "Date": {
      "Date": datetime.date(2017, 12, 10),
      "Attribute": datetime.date(2017, 12, 10).weekday(),
      "Season": 2
    }, 
    "Final Date": datetime.date(2018, 3, 19), #hay que cambiarlo, me lo he inventado
    "Weather": "Rain",
    "Traffic": {
      "Total": None,
      "Children": None,
      "Teenagers": None,
      "Adults": None,
      "Olders": None
    }, 
  }
  return initialState_Dict, dictList