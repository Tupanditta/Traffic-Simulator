"""
Definir la fecha exacta del inicio de la simulación

Establecer un clima inicial por defecto para el día 0, de ahí calculará el motor 
climático el temporal del día uno

Inicializar la estructura vacía donde iremos recopilando la información
"""

def create_InitialState(context_dict):
  dictList = [] #los diccionarios de cada día se guardarán en un lista
  initialState_Dict = {
    "Date": {
      "Year": 2017,
      "Month": None,
      "Day": None,
      "Attribute": None,
      "Season": None
    }, 
    "Weather": None,
    "Traffic": {
      "Total": None,
      "Children": None,
      "Teenagers": None,
      "Adults": None,
      "Olders": None
    }, 

  

  }
  return initialState_Dict, dictList