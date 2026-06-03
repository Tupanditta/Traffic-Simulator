"""
Este será el bucle while encargado de llamar a las funciones necesarias, 
y así en cada iteración se simulará un día. 

Creará los datos y los almacenará en la estructura de datos ubicada en el archivo 
state
"""

from engine.InitialState.initialState import variables, create_initial_state
from engine.environment.calendary import create_date
from engine.environment.weather import update_weather
from engine.traffic.traffic_calculator import calculate_traffic
from engine.accidents.accidents_calculator import calculate_accidents
import pprint #para imprimir diccionarios en las ejecuciones de prueba

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
        actual_date_dict = calculate_traffic(actual_date_dict, context_dict)

        ###### 3. CALL CALCULATOR
        # Calcula los accidentes ocurridos ese día en función de todos los datos ya obtenidos
        actual_date_dict = calculate_accidents(actual_date_dict, context_dict)

        ###### 4. CALL UPDATE DATAS
        # Guarda todos los datos obtenidos y creados y actualiza el state
        dict_list.append(actual_date_dict)
        
        ###### 5. CALL NEXT
        # Avanzamos un día para que el bucle no sea infinito y guardamos el clima de hoy en la variable
        # del clima de ayer
        yesterday_date_dict = actual_date_dict
        yesterday_date = actual_date_dict["date"]["date"]
        pprint.pprint(actual_date_dict)

    return dict_list
