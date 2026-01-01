import pandas as pd
import requests
import json

# Will need to pull all years
zipcode = input("zip: ")
#2011-2023
years = [year for year in range(2016,2018)]
DPs = ["DP02","DP03","DP04","DP05"]
results = []
vars = []
exclude = ["GEO_ID", "NAME", "ucgid"] #, "DP05_0020E", "DP05_0019E" "DP05_0028E", "DP05_0032E", "DP05_0004E"]

# Two categories; variables added in subsequent years, and variables adjusted
exclude_years = [
    [],
    []
]
# etc.

for year in years:
    if min(years) == 2011: # exclude variables added after min year
        exclude.append(one)
    
    temp = {}
    if year > 2020:
        x = "Z2"
    else:
        x = "00"
    for DP in DPs:
        # REMOVE KEY BEFORE PUBLISH
        url = f"https://api.census.gov/data/{year}/acs/acs5/profile?get=group({DP})&ucgid=860{x}00US{zipcode}&key=915657d4de9518c7ed7dc042dd08050606fa1492"
        response = requests.get(url)
        for var, stat in zip(response.json()[0],response.json()[1]):
            if var not in exclude and all(w not in var.split("_")[1] for w in ["M","P","A"]):
                vars.append(var)
            
            if var in vars:
                if year == x:
                    var = # var from 2011, etc.
                if stat == -888888888:
                    temp[var] = 0
                else:
                    temp[var] = stat
    df_temp = pd.DataFrame(temp, index = [year])
    results.append(df_temp)

print(results)

df = pd.concat(results, axis = 0, join = "inner")

#print(df)

# with open('variables.json', 'r') as file:
#     variables = json.load(file)
# variables = variables["variables"]
# for v in variables.items():
#     label = v[1]["label"].split("!!",1) #.replace("!!",", ")
#     if len(label) > 1: 
#         label = label[1].replace("!!", ", ").lower()
#     for i in df.columns:
#         if v[0] == i:
#             df.rename(columns={i: label}, 
#                       inplace = True)

#print(df)

df.to_csv('test.csv')
