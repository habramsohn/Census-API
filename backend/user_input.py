# Rewrite to accomodate JSON GET requests when known

# Get user wants
def basic_input(zipcode, min_year, max_year):
    zipcode = zipcode
    min_year = min_year
    max_year = max_year
    years = list(range(min_year, max_year+1))
    year_len = len(years)
    # Robustness checks
    return zipcode, years, year_len

# Discover if user wants CSV or not
def csv_check():
    csv_check = "no - temp"
    if csv_check == "Yes":
        csv_bool = True
    else:
        csv_bool = False
    return csv_bool

if __name__ == "__main__":
    user_input()
    csv_check()