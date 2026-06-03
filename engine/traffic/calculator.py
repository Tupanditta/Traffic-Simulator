from typing import TypedDict

def calculate_traffic(actual_date_dict, context_dict):
  population = context_dict["population"]
  weather = actual_date_dict["weather"]

  demography_groups_dict: dict = context_dict["demography"]
  # traffic_exposure_percentages_dict: dict = context_dict["traffic_exposure_percentages"]
  weather_traffic_multipliers_dict: dict = context_dict["weather_traffic_multipliers"]

  total_traffic = 0

  for group in demography_groups_dict.keys():
    group_traffic = population * (demography_groups_dict[group] / 100) * weather_traffic_multipliers_dict[group][weather]
    actual_date_dict["traffic"][group] = int(group_traffic)
    total_traffic += int(group_traffic)

  actual_date_dict["traffic"]["total"] = total_traffic

  return actual_date_dict