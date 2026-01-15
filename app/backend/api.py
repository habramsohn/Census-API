import pandas as pd
import requests
import json
import itertools

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

def api_fun(api_key, year, zipcode, vars, results):
    DPs = ["DP02","DP03","DP04","DP05"]
    temp = {}
    if year > 2020:
        x = "Z2"
    else:
        x = "00"
    for dp in DPs:
        url = f"https://api.census.gov/data/{year}/acs/acs5/profile?get=group({dp})&ucgid=860{x}00US{zipcode}&key={api_key}"
        print(url)
        temp = dp_fun(url, vars, year, temp)                                                                    
    results.append(pd.DataFrame(temp, index = [year]))
    print(f"{year} complete!")
    return results
    
def dp_fun(url, vars, year, temp):
    response = requests.get(url)
    zipped = zip(response.json()[0],response.json()[1])
    for var, stat in zipped:
        if var in vars:
            mutate = mutate_fun(year, var)
            key = mutate.get(var, var)
            temp[key] = max(0, float(stat))
    return temp

def mutate_fun(year, var):
    mutate = {}
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
    return mutate

def rename_fun(df, variables):
    mapping = {name: var["label"].split("!!",1)[1].lower().replace("!!",", ") for name, var in variables.items() if name in df.columns}
    df.rename(columns=mapping, inplace=True)

def main_fun(api_key, zipcode, years):
    results = []
    variables = variables_fun()
    vars = []
    [vars.append(var) for var in variables if include_fun(var) == True]
    [api_fun(api_key, year, zipcode, vars, results) for year in years]
    df = pd.concat(results, axis = 0)
    rename_fun(df, variables)
    return df

if __name__ == "__main__":
    main_fun()