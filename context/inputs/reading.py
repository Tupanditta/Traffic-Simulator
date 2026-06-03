"""
Este módulo es el que tiene las funciones input() del simulador
Es el único módulo que tiene dichas funciones, en todo el proyecto no habrá otro archivo.py que use esta función

Se ayuda del módulo validator.py para validar si las entradas del usuario son válidas

Si alguna entrada no es válida, se vuelve a pedir de nuevo
  Por lo que el usuario debe introducir TODOS los datos, y BIEN
  
  Si algún dato no se introduce correctamente, solo se pide dicho dato de nuevo, 
  los datos introducidos previamente (son correctos) permanecen inalterados
  
  El que el dato introducido sea correcto dependerá de las fucniones implementadas
  en el archivo validator.py
  Por lo que hacer un cambio tanto en validator.py como en reading.py puede afectar al otro 
"""

from .validator import validate_demography, validate_population, validate_risk_factors, validate_temporality, pass_temporality_options

def ask_temporality() -> int:
  """
  Por ahora el valor temporality serán una de las cuatro estaciones (un valor int en este caso): 
    1 = Verano
    2 = Invierno
    3 = Otoño
    4 = Primavera

  voy a guardarlos en un diccionario; el valor de temporality será la clave del valor (estación)
  """
  temporality_options = pass_temporality_options() # devuelve un dict con las opciones
  
  for key, value in temporality_options.items(): 
    print(f"Opción {key}: {value}", end="\n") # Visual

  while True:
    try:
      # Hacemos la petición al usuario de la estación del mes
      temporality = int(input("Introduzca el número de una de las opciones: "))

      # Verificamos que ha escogido una de las opciones 
      if validate_temporality(temporality): 
        return temporality 
      
    except ValueError:
      # Esta línea solo se ejecuta si el valor de temporality son letras, símbolos
      print("[ERROR] Entrada no válida. Se debe introducir un valor numérico entero\n")

def ask_population() -> int:
  """
  El valor de population será un integer que determinará cual es la población actual de la zona
  """
  while True:
    try:
      # Hacemos la petición al usuario de la población 
      population = int(input("Introduzca el número (int) de la población actual: \n"))

      # Verificar que el dato es un entero mayor que 0 
      if validate_population(population): 
        return population
    
    except ValueError:
      # Esta línea solo se ejecuta si el valor de population son letras, símbolos 
      print("[ERROR] Entrada no válida. Se debe introducir un valor numérico entero\n")

def ask_risk_factors():
  """
  Pide al usuario los porcentajes de consumo de alcohol y drogas por franja de edad.
  """
  risk_factors = { 
    "alcohol" : {
      "children": None,
      "teenagers": None,
      "adults" : None, 
      "olders" : None
    },
    "drugs" : {
      "children": None,
      "teenagers": None,
      "adults" : None, 
      "olders" : None
    }
  }

  for factor in risk_factors:
    print(f"Factor: {factor}") # Visual
    for i in risk_factors[factor].keys(): # Dentro del factor, recorrer las diferentes edades
      while True:
        try: 
          # Hacemos la petición al usuario
          risk_factor_percent = float(input(f"Introduce qué porcentaje de los {i} consume {factor}: ")) 

          # Validar que el dato es correcto
          if validate_risk_factors(risk_factor_percent): 
            risk_factors[factor][i] = risk_factor_percent
            break
        except ValueError:
          # Esta línea solo se ejecuta si el valor son letras, símbolos
          print("[ERROR] Entrada no válida. Se debe introducir un valor numérico válido\n")

  return risk_factors

def ask_demography():
  """
  Puede que con los primeros campos la suma llegue a 100
  En tal caso los casos restantes se quedarán a 0
  """
  demography = {
    "children" : 0, 
    "teenagers": 0, 
    "adults" : 0, 
    "olders" : 0,   
  }
  parcial_percents_sum = 0 # Inicializo la suma de los porcentajes
  cont_percents_saved = len(list(demography.keys())) - 1 

  for i in demography:
    while True:
      try:
        if parcial_percents_sum >= 100:
          break # Ya he llegado al 100%
        elif cont_percents_saved > 0: # Mientras no esté en la última clave
          demography_percent = float(input(f"Introduce qué porcentaje de la población es {i}: "))
          if validate_demography(demography_percent, parcial_percents_sum):  # Valido la entrada
            parcial_percents_sum += demography_percent 
            demography[i] = demography_percent 
            cont_percents_saved -= 1 
            break
        else:
          demography[i] = 100 - parcial_percents_sum # Calculo el último valor
          break

      except ValueError:
        # Esta línea solo se ejecuta si el valor son letras o símbolos
          print("[ERROR] Entrada no válida. Se debe introducir un valor numérico válido\n")

  return demography