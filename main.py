from context.create_context import create
from engine.runner import run
from formatters.conversion_manager import execute_conversion
from persistence.export_manager import execute_exports

context_dict = create()
dict_list = run(context_dict)

dict_list, context_dict = execute_conversion(dict_list, context_dict)

execute_exports(dict_list, context_dict)

