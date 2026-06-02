# Importamos la FUNCIÓN read_statisticalDatas desde el archivo statisticalData_reading
from context.statisticalData.statisticalData_reading import read_statisticalDatas

# Importamos la FUNCIÓN user_datas desde el archivo data_dictionary
from context.inputs.data_dictionary import user_datas

def create():
  # Llamamos a las funciones correctamente
  userInputsDict = user_datas()
  statisticalDataDict = read_statisticalDatas()

  # Fusionamos los diccionarios
  context_dict = userInputsDict | statisticalDataDict
  
  return context_dict