import datetime
from typing import TypedDict

def create_date(yesterday_date_dict):
  actual_date_dict = {
    "Date": {
      "Date": None,
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
  yesterday_date: datetime.date = yesterday_date_dict["Date"]["Date"] #para que reconozca el tipo de dato

  oneDay = datetime.timedelta(days=1)

  actual_day = yesterday_date + oneDay

  actual_date_dict["Date"]["Date"] = actual_day
  actual_date_dict["Date"]["Attribute"] = actual_day.weekday()
  actual_date_dict["Date"]["Season"] = yesterday_date_dict["Date"]["Season"]
  
  return actual_date_dict