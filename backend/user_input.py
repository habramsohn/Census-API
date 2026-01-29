# Legacy code to define zipcode and year range as requested by user; modularized for future updates as applicable 
def basic_input(zipcode, min_year, max_year):
    zipcode = zipcode
    min_year = min_year
    max_year = max_year
    years = list(range(min_year, max_year + 1))
    year_len = len(years)
    return zipcode, years, year_len