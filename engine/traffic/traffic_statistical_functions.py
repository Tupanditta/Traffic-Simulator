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