from api import main_fun
from export import export 
from user_input import user_input, csv_check
import visual
import wrangling

def execute():
    # User input
    zip, min_year, max_year = user_input()
    check_bool = csv_check()
    # API and data wrangling
    df = main_fun(zip, min_year, max_year)
    # End products
    export(check_bool, df)

if __name__ == "__main__":
    execute()