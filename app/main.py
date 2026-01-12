from api import main_fun
from export import export 
from user_input import basic_input, csv_check, variable_input
from visual import visualize
from wrangling import wrun
from test import test
import os
api = "915657d4de9518c7ed7dc042dd08050606fa1492"
#api = os.environ.get('API')

def execute():
    # User input - Get requested zip, year range, and desire for CSV export
    zipcode, years, year_len = basic_input()
    check_bool = csv_check()
    # API
    df = main_fun(zipcode, years, api)
    repeat = "Yes"
    while repeat == "Yes":
        #temp
        arg = test()
        variable_input(arg)
        #Wrangle
        new_df, export_df = wrun(df, arg)
        # exports products
        try:
            visualize(arg, new_df, year_len)
        except Exception as e:
            print(e)
            pass
        repeat = input("repeat? ")
    export(check_bool, export_df)

if __name__ == "__main__":
    execute()