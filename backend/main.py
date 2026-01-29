from backend import api, info, user_input, visual, wrangling
data = info.data

# Use user input to request data from Census website
def execute_df(api_key, zipcode="23185", min_year=2021, max_year=2022):
    # User input - Get requested zip, year range, and desire for CSV export
    zipcode, years, year_len = user_input.basic_input(zipcode, min_year, max_year)
    # API
    df = api.main_fun(api_key, zipcode, years)
    return df, year_len


# Reconstitute DataFrame to contain specified variable, then generate dynamic plot 
def execute_viz(df, year_len, arg="income"):
    new_df = wrangling.wrun(df, arg, data)
    plot_html = visual.visualize(arg, year_len, new_df, data)
    return plot_html


# Export all pulled data if requested
def export_csv(df):
    export_df = wrangling.wrangle_csv(df)
    return export_df