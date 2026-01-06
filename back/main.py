from api import main_fun
from export import export 
from user_input import basic_input, csv_check, variable_input
import visual
import wrangling
from test import test
import os
api = "915657d4de9518c7ed7dc042dd08050606fa1492"
#api = os.environ.get('API')

def execute():
    # User input - Get requested zip, year range, and desire for CSV export
    #zip, min_year, max_year = basic_input()
    #check_bool = csv_check()
    # API and data wrangling
    #df = main_fun(zip, min_year, max_year, api)
    arg = test()
    variable_input(arg)

    # End products
    #export(check_bool, df)

if __name__ == "__main__":
    execute()

# Zip, year range, csv -> user_input -> api ->  export (if yest) -> user -> 
# selected variable -> user_input -> wrangling -> visualization -> user
# Start with aggregate information, expand submenus later if desired