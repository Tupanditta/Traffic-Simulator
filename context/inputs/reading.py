"""
Este módulo es el que tiene las funciones input() del simulador
Es el único módulo que tiene dichas funciones, en todo el proyecto no habrá otro archivo.py que use esta función

Se ayuda del módulo py para validar si las entradas del usuario son válidas

Si alguna entrada no es válida, se vuelve a pedir de nuevo
  Por lo que el usuario debe introducir TODOS los datos, y BIEN
  
  Si algún dato no se introduce correctamente, solo se pide dicho dato de nuevo, 
  los datos introducidos previamente (son correctos) permanecen inalterados
  
  El que el dato introducido sea correcto dependerá de las fucniones implementadas
  en el archivo validator.py
  Por lo que hacer un cambio tanto en validator.py como en rading.py puede afectar al otro 
"""

from .validator import validate_demography, validate_population, validate_riskFactors, validate_temporality, pass_temporality_options

def ask_temporality() -> int:
  """
  Por ahora el valor temporality serán una de las cuatro estaciones (un valor int en este caso): 
    1 = Verano
    2 = Invierno
    3 = Otoño
    4 = Primavera

  voy a guardarlos en un diccionario; el valor de temporality será la clave del valor (estación)
  """
  temporality_options = pass_temporality_options() #devuelve un dict con las opciones
  
  for key, value in temporality_options.items(): print(f"Opción {key}: {value}", end="\n") #Visual

  while True:
    try:
      #Hacemos la petición al usuario de la estación del mes
      temporality = int(input("Introduzca el número de una de las opciones: "))

      #Verificamos que ha escogido una de las opciones 
      if validate_temporality(temporality): return temporality 
      
    except ValueError:
      #Esta línea solo se ejecuta si el valor de temporality son letras, símbolos
      print("[ERROR] Entrada no válida. Se debe introducir un valor numérico entero\n")

def ask_population() -> int:
  """
  El valor de population será un integer que determinará cual es la población actual de la zona
  """
  while True:
    try:
      #Hacemos la petición al usuario de la población 
      population = int(input("Introduzca el número (int) de la población actual: \n"))

      #Verificar que el dato es un entero mayor que 0 
      if validate_population(population): return population
    
    except ValueError:
      #Esta línea solo se ejecuta si el valor de population son letras, símbolos 
      print("[ERROR] Entrada no válida. Se debe introducir un valor numérico entero\n")

def ask_riskFactors():
  """

  """
  riskFactors = { #creo el diccionario
    "alcohol" : {
      "teenagers": None,
      "adults" : None, 
      "olders" : None
    },
    "drugs" : {
      "teenagers": None,
      "adults" : None, 
      "olders" : None
    }
  }

  for factor in riskFactors:
    print(f"Factor: {factor}") #visual
    for i in riskFactors[factor].keys(): #dentro del factor, recorrer las diferentes edades
      while True:
        try: 
          #Hacemos la petición al usuario del porcentaje de dicho rango de la población que consume dicho factor
          riskFactor_percent = float(input(f"Introduce que porcentaje de los {i} consume {factor}: ")) 

          #Validar que el dato es correcto
          if validate_riskFactors(riskFactor_percent): 
            riskFactors[factor][i] = riskFactor_percent
            break
        except ValueError:
          #Esta línea solo se ejecuta si el valor del porcentaje del factor de riesgo (riskFactor_percent) son letras, símbolos
          print("[ERROR] Entrada no válida. Se debe introducir un valor numérico válido\n")

  return riskFactors

def ask_demography():
  """
  puede que con los primeros campos la suma llegue a 100
  en tal caso los casos restantes se quedarán a 0
  """
  demography = {
    "children" : 0, 
    "Teenagers": 0,
    "adults" : 0, 
    "older" : 0,
  }
  parcial_percents_sum = 0 #inicializo la suma de los porcentajes
  cont_percents_saved = len(list(demography.keys())) - 1 

  for i in demography:
    while True:
      try:
        if parcial_percents_sum >= 100:
          break #ya he llegado al 100%
        elif cont_percents_saved > 0: #mientras no este en la última clave
          demography_percent = float(input(f"Introduce que porcentaje de la población es {i}: "))
          if validate_demography(demography_percent, parcial_percents_sum):  #valido la entrada
            parcial_percents_sum += demography_percent #calculo la suma parcial de todos los porcentajes introducidos
            demography[i] = demography_percent #añado el nuevo valor
            cont_percents_saved -= 1 #voy contando cuantos campos he llenado hasta el momento
            break
        else:
          demography[i] = 100 - parcial_percents_sum #calculo el último valor en base al valor de los anteriores
          break

      except ValueError:
        #Esta línea solo se ejecuta si el valor del porcentaje son letras o símbolos
          print("[ERROR] Entrada no válida. Se debe introducir un valor numérico válido\n")

  return demography
