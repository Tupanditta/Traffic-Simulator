"""
Crea el diccionario para el nuevo día

Da valores a date, attribute y season

Para calcular todos los valores se basa en el día de ayer
"""

import datetime

def create_date(yesterday_date_dict: dict) -> dict:
  actual_date_dict = {
    "date": {
      "date": None,
      "attribute": None,
      "season": None
    }, 
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
  }
  yesterday_date: datetime.date = yesterday_date_dict["date"]["date"] # para que reconozca el tipo de dato

  one_day = datetime.timedelta(days=1)

  actual_day = yesterday_date + one_day

  actual_date_dict["date"]["date"] = actual_day
  actual_date_dict["date"]["attribute"] = actual_day.weekday()
  actual_date_dict["date"]["season"] = yesterday_date_dict["date"]["season"]
  
  return actual_date_dict