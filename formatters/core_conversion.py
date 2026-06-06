"""
Hay que aislar la función que hace la conversión, esta luego se llama desde diferentes módulos 

Cuidado porque este módulo también se mete en diccionarios
"""

def do(sub_dict: dict, str_list: list) -> dict:
  """
  Realiza la conversión de un subdiccionario del context
  """
  new_sub_dict = {}

  for key, value in sub_dict.items():
    if str(key).isdigit():
      index = int(key) - 1
      if 0 <= index < len(str_list):
        str_value = str_list[index]
        new_sub_dict[str_value] = value
      else:
        new_sub_dict[key] = value
    else:
      new_sub_dict[key] = value

  return new_sub_dict