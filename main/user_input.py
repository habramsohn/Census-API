# User input to define:
## Zip code (to api)
## Year range (to api)
## Desired variables (to wrangling.py)
## export cvs? (to export.py)

def user_input():
    zip = input("Zip: ")
    min_year = int(input("Start year: "))
    max_year = int(input("End year: "))
    # Robustness checks
    return zip, min_year, max_year

def csv_check():
    csv_check = input("CSV? ")
    if csv_check == "Yes":
        csv_bool = True
    else:
        csv_bool = False
    return csv_bool

if __name__ == "__main__":
    user_input()
    csv_check()