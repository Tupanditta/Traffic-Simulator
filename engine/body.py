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
    "riskFactors": {
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
        "Teenagers": 0.0,  # OJO: Se mantiene el typo de tu código original
        "adults": 55.0,
        "older": 20.0
    },

    # ==========================================
    # DATOS ESTADÍSTICOS (read_statisticalDatas)
    # ==========================================
    "_comment_doc": "Archivo de configuracion principal del Simulador de Accidentes.",
    "_comment_matrix": "Probabilidades de transicion de Markov. Claves: Sun, Rain, Snow, Cloudy",
    "Transition_Matrix": {
        "Winter": {
            "Sun": {"Sun": 0.45, "Rain": 0.30, "Snow": 0.05, "Cloudy": 0.20},
            "Rain": {"Sun": 0.25, "Rain": 0.55, "Snow": 0.15, "Cloudy": 0.05},
            "Snow": {"Sun": 0.15, "Rain": 0.40, "Snow": 0.35, "Cloudy": 0.10},
            "Cloudy": {"Sun": 0.25, "Rain": 0.15, "Snow": 0.05, "Cloudy": 0.55}
        },
        "Spring": {
            "Sun": {"Sun": 0.65, "Rain": 0.30, "Snow": 0.01, "Cloudy": 0.04},
            "Rain": {"Sun": 0.45, "Rain": 0.50, "Snow": 0.03, "Cloudy": 0.02},
            "Snow": {"Sun": 0.40, "Rain": 0.50, "Snow": 0.10, "Cloudy": 0.00},
            "Cloudy": {"Sun": 0.70, "Rain": 0.20, "Snow": 0.00, "Cloudy": 0.10}
        },
        "Summer": {
            "Sun": {"Sun": 0.88, "Rain": 0.12, "Snow": 0.00, "Cloudy": 0.00},
            "Rain": {"Sun": 0.75, "Rain": 0.25, "Snow": 0.00, "Cloudy": 0.00},
            "Snow": {"Sun": 1.00, "Rain": 0.00, "Snow": 0.00, "Cloudy": 0.00},
            "Cloudy": {"Sun": 1.00, "Rain": 0.00, "Snow": 0.00, "Cloudy": 0.00}
        },
        "Autumn": {
            "Sun": {"Sun": 0.60, "Rain": 0.25, "Snow": 0.00, "Cloudy": 0.15},
            "Rain": {"Sun": 0.35, "Rain": 0.50, "Snow": 0.02, "Cloudy": 0.13},
            "Snow": {"Sun": 0.25, "Rain": 0.60, "Snow": 0.10, "Cloudy": 0.05},
            "Cloudy": {"Sun": 0.40, "Rain": 0.20, "Snow": 0.00, "Cloudy": 0.40}
        }
    },
    "_comment_base_rate": "Probabilidad pura de accidente por persona expuesta en condiciones ideales.",
    "Base_Accident_Rate": 0.00015,
    "_comment_exposure": "Porcentaje de la poblacion que sale a la calle segun el tipo de dia.",
    "Traffic_Exposure_Percentages": {
        "Children": {"Workday": 0.85, "Weekend": 0.60, "Holiday": 0.40},
        "Teenagers": {"Workday": 0.90, "Weekend": 0.75, "Holiday": 0.50},
        "Adults": {"Workday": 0.95, "Weekend": 0.65, "Holiday": 0.45},
        "Olders": {"Workday": 0.50, "Weekend": 0.40, "Holiday": 0.35}
    },
    "_comment_env_multipliers": "Como altera el clima la tasa base de siniestralidad.",
    "Environmental_Multipliers": {
        "Winter": {"Sun": 1.000, "Rain": 1.070, "Snow": 1.620, "Cloudy": 1.190},
        "Spring": {"Sun": 1.000, "Rain": 1.145, "Snow": 1.440, "Cloudy": 1.350},
        "Summer": {"Sun": 1.000, "Rain": 1.685, "Snow": 1.310, "Cloudy": 2.100},
        "Autumn": {"Sun": 1.000, "Rain": 1.240, "Snow": 1.855, "Cloudy": 1.520}
    },
    "_comment_beh_multipliers": "Como altera el comportamiento (alcohol/drogas) el riesgo individual.",
    "Behavioral_Multipliers": {
        "Alcohol": 3.0,
        "Drugs": 7.0,
        "Sober": 1.0
    }
}

import initialState

def run(context_dict):
    initialState_Dict, dictList = initialState.create_InitialState(context_dict)


###### 1. CALL ENVIRONMENT

### 1.1 CALL calendary.py
#Pasar la fecha actual al motor calendary.py, y este devuelve los atributos de esa fecha exacta


### 1.2 CALL clima.py
#Pasar el clima de ayer al motor clima.py y este devuelve el clima de hoy

###### 2. CALL CALCULATOR
#Calcula los accidentes ocurridos ese día en función de todos los datos ya obtenidos

###### 3. CALL UPDATE DATAS
#Guarda todos los datos obtenidos y creados y actualiza el state

###### 4. CALL NEXT
#Avanzamos un día para que el bucle no sea infinito y guardamos el clima de hoy en la variable
#del clima de ayer

    return dictList

