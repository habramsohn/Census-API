import pandas as pd
import requests
import json
import itertools

# Future improvements; all variable changes related to ancestry to include
# REWRITE CODE FOR PYTHONICISM 
## Nested logic -> dictionaries
## Apply with vectorization (e.g. df.rename(columns=mapping, inplace = T))
## Break into bespoke .py scripts and __main__.py file
# FUTURE
## Set up remote API call
## Refine variable offerings to speed up API call
## Build front-end visualization app
## Rewrite client-side API call to request only variables relevant to user query

# SCHEMA API 
## Add if __name__ == "main" scheme
## Functions:
### Variable declaration from JSON
### Variable mutations
### Variable exclusions
### Z2/00 declaration
### Accept user input ZIP Code
### Accept user input years range
### Pull years/DPs 
### Combine pulled years/DPs
### Replace variable API codes with variable labels

def mutate_fun(year, var):
    pref = var.split("_")[0]
    iter = int(var.split("_")[1].split("E")[0])
    dec = var.split("_")[1].split("E")[0]
    # Removed: Sex ratios, over 16 and under 18 categories 
    if year > 2016 and pref == "DP05":
        if iter > 4 and iter <= 18:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-1:04d}")) 
            #print(f"{year}, >4, <18,{var}")
        elif iter > 20 and iter <= 27: # and dec <= 20:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-3:04d}")) 
            #print(f"{year}, >20,{var}")
        elif iter > 28 and iter <= 32:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-4:04d}")) 
            #print(f"{year}, >27,{var}")
        elif iter > 32:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-5:04d}")) 
            #print(f"{year}, >31,{var}")
    # Removed: Cohabiting stats
    if year > 2018 and pref == "DP02":
        if iter > 14 and iter <= 20:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-1:04d}")) 
            #print(mutate[var])
        elif iter > 21 and iter <= 24:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-2:04d}"))
        elif iter > 24:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-1:04d}"))
    # Removed: Computer and internet access statistics
    if year > 2019 and pref == "DP02":
        if iter > 85:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-2:04d}"))
    if year > 2014 and pref == "DP04":
        if iter > 24:
            mutate[var] = var.replace(str(dec), str(f"{int(dec)-1:04d}"))
    return mutate

def exclude_fun(var):
    # Removed highly specific household description
    a = [f"DP02_{n:04d}E" for n in range(3,15)]
    b = [f"DP05_{n:04d}E" for n in range(77,82)]
    c = ["DP02_0023E"]
    exclude = list(itertools.chain(a,c))
    if len(var.split("_")) > 1 and all(w not in var.split("_")[1] for w in ["M","P","A","ID"]) and "PR" not in var.split("_")[0] and var not in exclude:
        return True
    else:
        return False

# Will need to pull all years
#start = input("Start year: ")
#end = input("End year: ")
zipcode = input("zip: ")
#2011-2023
years = [year for year in range(2011,2024)]
DPs = ["DP02","DP03","DP04","DP05"]
results = []
# 2011 variables
with open('variables.json', 'r') as file:
    variables = json.load(file)
variables = variables["variables"]
vars = []
for var in variables:
    if exclude_fun(var) == True:
        vars.append(var)

for year in years:
    temp = {}
    mutate = {}
    data = {}
    if year > 2020:
        x = "Z2"
    else:
        x = "00"
    for DP in DPs:
        # REMOVE KEY BEFORE PUBLISH
        url = f"https://api.census.gov/data/{year}/acs/acs5/profile?get=group({DP})&ucgid=860{x}00US{zipcode}&key=915657d4de9518c7ed7dc042dd08050606fa1492"
        response = requests.get(url)
        for var, stat in zip(response.json()[0],response.json()[1]):
            if var in vars:
                mutate_fun(year, var)
                if var in mutate:
                    if float(stat) < 0:
                        temp[mutate[var]] = 0
                    else:
                        temp[mutate[var]] = stat
                else:
                    if float(stat) < 0:
                        temp[var] = 0
                    else:
                        temp[var] = stat
    df_temp = pd.DataFrame(temp, index = [year])
    results.append(df_temp)
    print(f"Year {year} pulled")

df = pd.concat(results, axis = 0)

for v in variables.items():
    label = v[1]["label"].split("!!",1) #.replace("!!",", ")
    if len(label) > 1: 
        label = label[1].replace("!!", ", ").lower()
    for i in df.columns:
        if v[0] == i:
            df.rename(columns={i: label}, 
                      inplace = True)

print(df)

df.to_csv('test.csv')
