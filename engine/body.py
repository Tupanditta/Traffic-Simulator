"""
Este será el bucle while encargado de llamar a las funciones necesarias, 
y así en cada iteración se simulará un día. 

Creará los datos y los almacenará en la estructura de datos ubicada en el archivo 
state
"""

context_dict = {
    # ==========================================
    # INPUTS ESTÁTICOS DEL USUARIO (user_datas)
    # ==========================================
    "temporality": 2,  # 1: Verano, 2: Invierno, 3: Otoño, 4: Primavera
    "population": 50000,
    "risk_factors": {
        "alcohol": {
            "teenagers": 15.5,
            "adults": 60.0,
            "olders": 20.0
        },
        "drugs": {
            "teenagers": 5.0,
            "adults": 10.0,
            "olders": 2.0
        }
    },
    "demography": {
        "children": 15.0,
        "teenagers": 10.0,
        "adults": 55.0,
        "olders": 20.0
    },

    # ==========================================
    # DATOS ESTADÍSTICOS (read_statistical_data)
    # ==========================================
    "_comment_doc": "Archivo de configuracion principal del Simulador de Accidentes.",
    "_comment_matrix": "Probabilidades de transicion de Markov. Claves: sun, rain, snow, cloudy",
    "transition_matrix": {
        "posible_states": ["sun", "rain", "snow", "cloudy"],
        1: {
            "sun": {"sun": 0.45, "rain": 0.30, "snow": 0.05, "cloudy": 0.20},
            "rain": {"sun": 0.25, "rain": 0.55, "snow": 0.15, "cloudy": 0.05},
            "snow": {"sun": 0.15, "rain": 0.40, "snow": 0.35, "cloudy": 0.10},
            "cloudy": {"sun": 0.25, "rain": 0.15, "snow": 0.05, "cloudy": 0.55}
        },
        2: {
            "sun": {"sun": 0.65, "rain": 0.30, "snow": 0.01, "cloudy": 0.04},
            "rain": {"sun": 0.45, "rain": 0.50, "snow": 0.03, "cloudy": 0.02},
            "snow": {"sun": 0.40, "rain": 0.50, "snow": 0.10, "cloudy": 0.00},
            "cloudy": {"sun": 0.70, "rain": 0.20, "snow": 0.00, "cloudy": 0.10}
        },
        3: {
            "sun": {"sun": 0.88, "rain": 0.12, "snow": 0.00, "cloudy": 0.00},
            "rain": {"sun": 0.75, "rain": 0.25, "snow": 0.00, "cloudy": 0.00},
            "snow": {"sun": 1.00, "rain": 0.00, "snow": 0.00, "cloudy": 0.00},
            "cloudy": {"sun": 1.00, "rain": 0.00, "snow": 0.00, "cloudy": 0.00}
        },
        4: {
            "sun": {"sun": 0.60, "rain": 0.25, "snow": 0.00, "cloudy": 0.15},
            "rain": {"sun": 0.35, "rain": 0.50, "snow": 0.02, "cloudy": 0.13},
            "snow": {"sun": 0.25, "rain": 0.60, "snow": 0.10, "cloudy": 0.05},
            "cloudy": {"sun": 0.40, "rain": 0.20, "snow": 0.00, "cloudy": 0.40}
        }
    },
    "_comment_base_rate": "Probabilidad pura de accidente por persona expuesta en condiciones ideales.",
    "base_accident_rate": 0.00015,
    "_comment_exposure": "Porcentaje de la poblacion que sale a la calle segun el tipo de dia.",
    "traffic_exposure_percentages": {
        "children": {"workday": 0.85, "weekend": 0.60, "holiday": 0.40},
        "teenagers": {"workday": 0.90, "weekend": 0.75, "holiday": 0.50},
        "adults": {"workday": 0.95, "weekend": 0.65, "holiday": 0.45},
        "olders": {"workday": 0.50, "weekend": 0.40, "holiday": 0.35}
    },
    "_comment_env_multipliers": "Como altera el clima la tasa base de siniestralidad.",
    "environmental_multipliers": {
        "winter": {"sun": 1.000, "rain": 1.070, "snow": 1.620, "cloudy": 1.190},
        "spring": {"sun": 1.000, "rain": 1.145, "snow": 1.440, "cloudy": 1.350},
        "summer": {"sun": 1.000, "rain": 1.685, "snow": 1.310, "cloudy": 2.100},
        "autumn": {"sun": 1.000, "rain": 1.240, "snow": 1.855, "cloudy": 1.520}
    },
    "_comment_beh_multipliers": "Como altera el comportamiento (alcohol/drogas) el riesgo individual.",
    "behavioral_multipliers": {
        "alcohol": 3.0,
        "drugs": 7.0,
        "sober": 1.0
    },
    "_comment_weather_traffic": "Multiplicador que reduce o mantiene la poblacion en la calle segun el clima.",
    "weather_traffic_multipliers": {
        "children": {"sun": 1.00, "cloudy": 0.95, "rain": 0.60, "snow": 0.20},
        "teenagers": {"sun": 1.00, "cloudy": 0.95, "rain": 0.75, "snow": 0.40},
        "adults": {"sun": 1.00, "cloudy": 0.98, "rain": 0.90, "snow": 0.75},
        "olders": {"sun": 1.00, "cloudy": 0.90, "rain": 0.40, "snow": 0.10}
    }
}

from engine.InitialState.initialState import variables, create_initial_state
from engine.environment.calendary import create_date
from engine.environment.weather import update_weather

def run(context_dict):
    # Crear el diccionario del estado inicial
    initial_state_dict, dict_list = create_initial_state(context_dict)

    # Pasar los datos necesarios del initial_state_dict a variables
    yesterday_date, yesterday_date_dict, final_date = variables(initial_state_dict)

    while yesterday_date < final_date:

        ###### 1. CALL ENVIRONMENT

        ### 1.1 CALL calendary.py
        # Pasar la fecha actual al motor calendary.py, y este devuelve los atributos de esa fecha exacta
        actual_date_dict = create_date(yesterday_date_dict)

        ### 1.2 CALL clima.py
        # Pasar el clima de ayer al motor clima.py y este devuelve el clima de hoy
        actual_date_dict = update_weather(context_dict, actual_date_dict, yesterday_date_dict)

        ###### 2. CALL TRAFFIC
        # Calcular tanto el tráfico total como el de cada grupo de edad

        ###### 3. CALL CALCULATOR
        # Calcula los accidentes ocurridos ese día en función de todos los datos ya obtenidos

        ###### 4. CALL UPDATE DATAS
        # Guarda todos los datos obtenidos y creados y actualiza el state

        ###### 5. CALL NEXT
        # Avanzamos un día para que el bucle no sea infinito y guardamos el clima de hoy en la variable
        # del clima de ayer
        yesterday_date_dict = actual_date_dict
        yesterday_date = actual_date_dict["date"]["date"]

    return dict_list