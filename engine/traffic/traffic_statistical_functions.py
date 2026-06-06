"""
Contiene las fórmulas necesarias para calcular el tráfico

Estas fórmulas no sabe de la existencia de diccionarios, solo 
recibe parámetros numéricos y hace el cálculo
"""

def calculate_group_traffic(population: int, demography_percent: float, weather_multiplier: float, traffic_exposure_percentage: float):
  """
  Calcula el tráfico de cada grupo demográfico
  """
  population = int(population)
  demography_percent = float(demography_percent)
  weather_multiplier = float(weather_multiplier)
  traffic_exposure_percentage = float(traffic_exposure_percentage)

  group_traffic = population * (demography_percent/100) * weather_multiplier * traffic_exposure_percentage

  return group_traffic