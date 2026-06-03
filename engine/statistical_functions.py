"""
Se implementan las fórmulas matemáticas y estadísticas que se van a usar
para con los datos del usuario recogidos (con el módulo inputs) y los datos
estadísticos leídos con stadisticalData_reading.py crear los datos de la bases de datos

No obstante, este archivo solo conoce los parámetros de entrada de las funciones, 
no le interesa nada más. El sabe de la existencia de unos datos, pero no sabe para que
se van a usar o como o de donde provienen, tampoco los datos que genere sabrá a donde van a 
acabar. A este archivo solo le interesa calcular. 

Así se aisla de todo el código, y se sigue la independencia que se ha ido contruyendo a lo largo
del proyecto
"""

#Statistical function para engine.traffic.traffic_calculator.calculate_traffic
def calculate_group_traffic(population, demography_percent, weather_multiplier, traffic_exposure_percentage):
  """
  Calcula el tráfico de cada grupo demográfico
  """
  population = int(population)
  demography_percent = float(demography_percent)
  weather_multiplier = float(weather_multiplier)
  traffic_exposure_percentage = float(traffic_exposure_percentage)

  group_traffic = population * (demography_percent/100) * weather_multiplier * traffic_exposure_percentage

  return group_traffic

#Statistical function para engine.accidents.accidents_calculator
def calculate_risk_factor_multiplier(alcohol_percent, drugs_percent, alcohol_weight, drugs_weight, sober_weight):
  alcohol_percent = float(alcohol_percent)
  drugs_percent = float(drugs_percent)
  sober_percent = 100 - alcohol_percent - drugs_percent

  behavioral_multiplier_sum = (alcohol_percent*alcohol_weight) + (drugs_percent*drugs_weight) + (sober_percent*sober_weight)
  behavioral_multiplier = behavioral_multiplier_sum / 100

  return behavioral_multiplier


def calculate_group_accidents(traffic, base_accident_rate, weather_multiplier, behavioral_multiplier):
  group_accidents = int(traffic) * base_accident_rate * weather_multiplier * behavioral_multiplier
  return int(group_accidents)