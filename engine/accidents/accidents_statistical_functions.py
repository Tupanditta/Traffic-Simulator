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