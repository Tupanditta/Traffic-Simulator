"""
Esta acción se encarga de hacer la llamada a las acciones de pedir datos, 
acciones que se implementaron en el módulo reading.py

Crea el diccionario con los diferentes datos que introduce el usuario

En principio, lo único que va a salir de este módulo de inputs (que contiene los archivos reading.py, 
validator.py y data_dictionary.py) es este diccionario

Todo está estructurado de manera que los demás módulos solo sepan de la existencia de este all_data_dictionary, ni si quiera
se sabrá que funciones usa internamente la función user_datas()

Si existieran cambios en alguna función, a menos que se añadiera un nuevo data, esta función no cambiaría en absoluto
"""
from .reading import ask_demography, ask_temporality, ask_population, ask_riskFactors

def user_datas():
  ####  CREATE DATA DICTIONARY
  all_data_dictionary = {
  }

  ####  ASK AND VALIDATE ALL DATAS
  all_data_dictionary["temporality"] = ask_temporality() #devuelve un int
  all_data_dictionary["population"] = ask_population() #devuelve un int
  all_data_dictionary["riskFactors"] = ask_riskFactors() #devuelve un diccionario
  all_data_dictionary["demography"] = ask_demography() #devuelve un diccionario
  
  return all_data_dictionary

