"""
"""

from context.create_context import create
from engine.body import run

######### 1. PHASE
"""
Creamos el contexto, es decir, llamamos al módulo context al archivo create_context.py a la función create()
Obtenemos un diccionario con todos los datos que vamos a ir usando a lo largo de la ejecución

Esta primera fase está totalmente aislada del resto del código. Dicho de otras maneras, el 
módulo context no sabe de la existencia del resto de módulos. Y el resto de módulos saben que 
existe un diccionario con información, pero no saben como se ha creado ni de donde viene. 

Se han ubicado varios "cortafuegos" en los siguientes módulos para que si algo falla la ejecución
se detenga de forma limpia y segura
"""

context_dict = create()
run(context_dict)

