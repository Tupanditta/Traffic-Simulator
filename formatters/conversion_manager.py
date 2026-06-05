from formatters.context_dict_conversion import context_dict_str_conversion
from formatters.dict_list_conversion import dict_list_str_conversion

def execute_conversion(dict_list, context_dict):
  converted_dict_list = dict_list_str_conversion(dict_list)
  converted_context_dict = context_dict_str_conversion(context_dict)

  return converted_dict_list, converted_context_dict