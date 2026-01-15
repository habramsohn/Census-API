from . import api, export, user_input, visual, wrangling
import os

def execute(api_key, zipcode="23185", min_year=2021, max_year=2022):
    # User input - Get requested zip, year range, and desire for CSV export
    zipcode, years, year_len = user_input.basic_input(zipcode, min_year, max_year)
    check_bool = user_input.csv_check()
    # API
    df = api.main_fun(api_key, zipcode, years)
    arg = user_input.variable_input()
    new_df, export_df = wrangling.wrun(df, arg)
    plot_html = visual.visualize(arg, new_df, year_len)
    export.export(check_bool, export_df)

    return plot_html

if __name__ == "__main__":
    execute()