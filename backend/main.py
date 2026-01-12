from api import main_fun
from export import export 
from user_input import basic_input, csv_check, variable_input
from visual import visualize
from wrangling import wrun
import os

api = os.environ.get('API_KEY')

def execute():
    # User input - Get requested zip, year range, and desire for CSV export
    zipcode, years, year_len = basic_input()
    check_bool = csv_check()
    # API
    df = main_fun(zipcode, years, api)
    repeat = "Yes"
    while repeat == "Yes":
        arg = variable_input()
        new_df, export_df = wrun(df, arg)
        visualize(arg, new_df, year_len)
        repeat = input("repeat? ")
    export(check_bool, export_df)

if __name__ == "__main__":
    execute()