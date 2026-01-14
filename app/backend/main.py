from api import main_fun
from export import export 
from user_input import basic_input, csv_check, variable_input
from visual import visualize
from wrangling import wrun
import os

api = os.environ.get('API_KEY')

def execute():
    # User input - Get requested zip, year range, and desire for CSV export
    zipcode, years, year_len = basic_input(zipcode, min_year, max_year)
    check_bool = csv_check()
    # API
    df = main_fun(zipcode, years, api)
    arg = variable_input()
    new_df, export_df = wrun(df, arg)
    plot_html = visualize(arg, new_df, year_len)
    export(check_bool, export_df)

    return plot_html

if __name__ == "__main__":
    execute()