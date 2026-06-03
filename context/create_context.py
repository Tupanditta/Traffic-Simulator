# Importamos la FUNCIÓN read_statistical_data desde el archivo statisticalData_reading
from context.statisticalData.statisticalData_reading import read_statistical_data

# Importamos la FUNCIÓN user_datas desde el archivo data_dictionary
from context.inputs.data_dictionary import user_datas

def create():
  # Llamamos a las funciones correctamente
  user_inputs_dict = user_datas()
  statistical_data_dict = read_statistical_data()

  # Fusionamos los diccionarios
  context_dict = user_inputs_dict | statistical_data_dict
  
  return context_dict
