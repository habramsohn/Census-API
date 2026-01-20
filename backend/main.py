from backend import api, user_input, visual, wrangling
import os
import io

def execute_df(api_key, zipcode='23185', min_year=2021, max_year=2022):
    # User input - Get requested zip, year range, and desire for CSV export
    zipcode, years, year_len = user_input.basic_input(zipcode, min_year, max_year)
    # API
    df = api.main_fun(api_key, zipcode, years)
    return df, year_len
    
def execute_viz(df, year_len, arg='income'):
    new_df = wrangling.wrun(df, arg)
    plot_html = visual.visualize(arg, year_len, new_df)
    return plot_html

def export_csv(df):
    export_df = wrangling.wrangle_csv(df)
    return export_df

if __name__ == "__main__":
    df, year_len = execute_df()
    new_df = execute_viz(df, year_len)
    export_df(new_df)