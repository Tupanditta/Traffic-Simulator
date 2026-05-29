from .statisticalData import statisticalData_reading
from .inputs import data_dictionary

def create():
  userInputsDict = data_dictionary()
  statisticalDataDict = statisticalData_reading()

  context_dict = userInputsDict | statisticalDataDict
  
  return context_dict