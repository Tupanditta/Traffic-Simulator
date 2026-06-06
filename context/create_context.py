"""
Es el módulo que dirige todo el context

Se encarga de llamar a la acción que pide los datos al usuario y de llamar a 
la función que lee y pasa los datos del json a un diccionario

Es independiente a inputs y a statistical_data, no sabe como funcionan estos, y si hubiera 
algún cambio en estos, es módulo quedaría inalterado

Luego unifica ambos diccionarios en uno solo, y este es el único dato que sale del context

De todo el context y sus módulos, la única función a la que se llama desde el main es esta

Este módulo crea diccionarios, pero en ningún momento se mete dentro de estos para nada
"""


from context.statistical_data.statistical_data_reading import read_statistical_data
from context.inputs.data_dictionary import user_datas

def create() -> dict:
  # Llamamos a las funciones correctamente
  user_inputs_dict = user_datas()
  statistical_data_dict = read_statistical_data()

  # Fusionamos los diccionarios
  context_dict = user_inputs_dict | statistical_data_dict
  
  return context_dict

