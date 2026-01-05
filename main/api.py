import pandas as pd
import requests
import json
import itertools

results = []
mutate = {}

def include_fun(var):
    cond_one = len(var.split("_")) > 1
    if cond_one:
        cond_two = all(w not in var.split("_")[1] for w in ["M","P","A","ID"]) and "PR" not in var.split("_")[0]
        if cond_two:
            return True
    else:
        return False

def variables_fun():
    with open('variables.json', 'r') as file:
        variables = json.load(file)
    variables = variables["variables"]
    return variables

def api_fun(year, zipcode, vars):
    DPs = ["DP02","DP03","DP04","DP05"]
    temp = {}
    if year > 2020:
        x = "Z2"
    else:
        x = "00"
    for dp in DPs:
        url = f"https://api.census.gov/data/{year}/acs/acs5/profile?get=group({dp})&ucgid=860{x}00US{zipcode}&key="
        temp = dp_fun(url, vars, year, temp)                                                                    
    results.append(pd.DataFrame(temp, index = [year]))
    
def dp_fun(url, vars, year, temp):
    response = requests.get(url)
    zipped = zip(response.json()[0],response.json()[1])
    for var, stat in zipped:
        if var in vars:
            mutate_fun(year, var)
            key = mutate.get(var, var)
            temp[key] = max(0, float(stat))
    return temp

def mutate_fun(year, var):
    pref = var.split("_")[0]
    num = int(var.split("_")[1].split("E")[0])
    dec = var.split("_")[1].split("E")[0]
    rules = {
        (2014, "DP04", 24): 1,
        (2016, "DP05", 4): 1,
        (2016, "DP05", 20): 3,
        (2016, "DP05", 28): 4,
        (2016, "DP05", 32): 5,
        (2018, "DP02", 14): 1,
        (2018, "DP02", 21): 2,
        (2018, "DP02", 24): 1,
        (2019, "DP02", 85): 2,
    }
    for rule, offset in rules.items(): 
        if year > rule[0] and pref == rule[1] and num > rule[2]:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-offset:04d}"))

def rename_fun(df, variables):
    mapping = {name: var["label"].split("!!",1)[1].lower().replace("!!",", ") for name, var in variables.items() if name in df.columns}
    df.rename(columns=mapping, inplace=True)

def main_fun(zip, min_year, max_year):
    years = list(range(min_year, max_year+1))
    variables = variables_fun()
    vars = []
    [vars.append(var) for var in variables if include_fun(var) == True]
    [api_fun(year, zip, vars) for year in years]
    df = pd.concat(results, axis = 0)
    rename_fun(df, variables)
    return df

if __name__ == "__main__":
    main_fun()

# csv_fun can be separated into a new script called when the user wants a table.

# FINISH
## Determine variables used for visualization
## 

# FUTURE
## Set up remote API call
## User error catching 
## Refine variable offerings to speed up API call
## Build front-end visualization app
### Start with biggest variables, go back and fix details in API call if wanted
## Rewrite client-side API call to request only variables relevant to user query

# Input -> API -> wrangle -> visual
