# Rewrite to accomodate JSON GET requests when known

# Get user wants
def basic_input():
    zipcode = input("Zip: ")
    min_year = int(input("Start year: "))
    max_year = int(input("End year: "))
    years = list(range(min_year, max_year+1))
    year_len = len(years)
    # Robustness checks
    return zipcode, years, year_len

# Discover if user wants CSV or not
def csv_check():
    csv_check = input("CSV? ")
    if csv_check == "Yes":
        csv_bool = True
    else:
        csv_bool = False
    return csv_bool

# Define desired variable 
def variable_input():
    arg = input("variable: ")
    return arg

if __name__ == "__main__":
    user_input()
    csv_check()