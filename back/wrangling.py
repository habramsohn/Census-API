# Reduce df to user-selected variable groups
def selection(arg):
    options = {
         'housing': ["households by type, total households", 
            "households by type, average household size",	
            "households by type, average family size",	
            "relationship, population in households"],
        'education': ["educational attainment, high school graduate (includes equivalency)",
        	"educational attainment, associate's degree",
            "educational attainment, bachelor's degree",
            "educational attainment, graduate or professional degree"],
        'culture': ["place of birth, native, born in united states, state of residence",
        	"place of birth, native, born in united states, different state",
            "place of birth, foreign born",
            "language spoken at home, english only",
            "language spoken at home, language other than english"],
        'employment': ["employment status, in labor force, civilian labor force, employed",
        	"employment status, in labor force, civilian labor force, unemployed",
            "employment status, not in labor force",
            "commuting to work, worked at home",
            "commuting to work, mean travel time to work (minutes)",
            "occupation, management, business, science, and arts occupations",
            "occupation, service occupations",
            "occupation, sales and office occupations",
            "occupation, natural resources, construction, and maintenance occupations",
            "occupation, production, transportation, and material moving occupations",
            "industry, agriculture, forestry, fishing and hunting, and mining",
            "industry, construction",
            "industry, manufacturing",
            "industry, wholesale trade",
            "industry, retail trade",	
            "industry, transportation and warehousing, and utilities",
            "industry, information",
            "industry, finance and insurance, and real estate and rental and leasing",
            "industry, professional, scientific, and management, and administrative and waste management services",
            "industry, educational services, and health care and social assistance",
            "industry, arts, entertainment, and recreation, and accommodation and food services",
            "industry, other services, except public administration",
            "industry, public administration",
            "class of worker, private wage and salary workers",
            "class of worker, government workers",
            "class of worker, self-employed in own not incorporated business workers"],
        'economic': ["income and benefits (in 2011 inflation-adjusted dollars), median household income (dollars)",
            "income and benefits (in 2011 inflation-adjusted dollars), mean household income (dollars)",
            "income and benefits (in 2011 inflation-adjusted dollars), median earnings for workers (dollars)",
            "housing occupancy, total housing units",	
            "housing occupancy, occupied housing units",
            "housing occupancy, vacant housing units",	
            "rooms, median rooms",
            "vehicles available, no vehicles available",
            "vehicles available, 1 vehicle available",
            "vehicles available, 2 vehicles available",
            "vehicles available, 3 or more vehicles available",
            "value, less than $50,000",
            "value, $50,000 to $99,999",
            "value, $100,000 to $149,999",
            "value, $150,000 to $199,999",
            "value, $200,000 to $299,999",
            "value, $300,000 to $499,999",
            "value, $500,000 to $999,999",
            "value, $1,000,000 or more",
            "value, median (dollars)"],
        'demographic': ["sex and age, male",
        	"sex and age, female",
            "sex and age, under 5 years",
            "sex and age, 5 to 9 years",
            "sex and age, 10 to 14 years",
            "sex and age, 15 to 19 years",
            "sex and age, 20 to 24 years",
            "sex and age, 25 to 34 years",
            "sex and age, 35 to 44 years",
            "sex and age, 45 to 54 years",
            "sex and age, 55 to 59 years",
            "sex and age, 60 to 64 years",
            "sex and age, 65 to 74 years",
            "sex and age, 75 to 84 years",
            "sex and age, 85 years and over",
            "sex and age, median age (years)"]}
    selected = options[arg]
    return selected

def wrangle(df, selected):
    new_df = df[selected]
    new_df.index.name = "year"
    return new_df

def wrun(df, arg):
    selected = selection(arg)
    new_df = wrangle(df, selected)
    return new_df

if __name__ == "__main__":
    wrun()