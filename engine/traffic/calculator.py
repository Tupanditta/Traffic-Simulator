from typing import TypedDict

def calculate_traffic(actual_date_dict, context_dict):
  population = context_dict["population"]
  weather = actual_date_dict["Weather"]

  demography_groups_dict: dict = context_dict["Demography"]
  #Traffic_Exposure_Percentages_dict: dict = context_dict["Traffic_Exposure_Percentages"]
  Weather_Traffic_Multipliers_dict: dict = context_dict["Weather_Traffic_Multipliers"]

  total_traffic = 0

  for group in demography_groups_dict.keys():
    group_traffic = population * (demography_groups_dict[group]/100) * Weather_Traffic_Multipliers_dict[group][weather]
    actual_date_dict["Traffic"][group] = int(group_traffic)
    total_traffic += int(group_traffic)

  actual_date_dict["Traffic"]["Total"] = total_traffic

  return actual_date_dict
