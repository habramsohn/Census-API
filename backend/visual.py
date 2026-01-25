import plotly.express as px
import pandas as pd
pd.options.mode.chained_assignment = None

def line(new_df, var, yaxis, title = None):
    if title == None:
        title = yaxis
    plot = px.line(new_df, x = new_df.index, y = var, title = f"{title} per Year", markers = True)
    plot.update_traces(name = yaxis, showlegend = True)
    plot.update_layout(xaxis_title = "Year", yaxis_title = f"{title}", xaxis = dict(tickmode = 'linear', gridcolor = 'lightgray', dtick = 1),
        yaxis = dict(gridcolor = 'lightgray'), yaxis_autorange = True, plot_bgcolor='white')
    return plot

def new_line(plot, new_df, var, yaxis):
    plot.add_scatter(x = new_df.index, y = new_df[var], mode = 'lines+markers', name = yaxis)
    plot.update_layout(yaxis_autorange=True)
    return plot

def bar(new_df, var, yaxis, title = None):
    if title == None:
        title = yaxis
    year = new_df.index[0]
    plot = px.bar(data_frame = new_df, x = new_df.index, y = var, title = f"{title} in {year}", color_continuous_scale = "Viridis")
    plot.update_traces(width = 0.4, opacity = 0.8, showlegend = True, name = yaxis)
    plot.update_layout(xaxis = dict(type = 'category', tickmode = 'array'), yaxis_title = title, xaxis_title = "Year", barmode = "group")
    return plot

def new_bar(plot, new_df, var, yaxis):
    plot.add_bar(x=new_df.index, y=new_df[var], name=yaxis)
    plot.update_layout(barmode="group")
    plot.update_traces(width = None)
    return plot

def visualize(arg, year_len, new_df): 
    data = {
        "population": [{"var": "relationship, population in households", "yaxis": "Total Population", "title": "Total Population"}],

        "education": [{"var": "educational attainment, high school graduate (includes equivalency)", "yaxis": "High School", "title": "Educational Attainment"},
        	        {"var": "educational attainment, associate's degree", "yaxis": "Associate's Degree"},
                    {"var": "educational attainment, bachelor's degree", "yaxis": "Bachelor's Degree"},
                    {"var": "educational attainment, graduate or professional degree", "yaxis": "Graduate Degree"}],

        "origin": [{"var": "place of birth, native, born in united states, state of residence", "yaxis": "State of Residence", "title": "Origin"},
        	    {"var": "place of birth, native, born in united states, different state", "yaxis": "Other U.S. State"},
                {"var": "place of birth, foreign born", "yaxis": "Foreign"}],

        "language": [{"var": "language spoken at home, english only", "yaxis": "Only English", "title": "Language Spoken at Home"},
                    {"var": "language spoken at home, language other than english", "yaxis": "Other than English"}],

        "occupation": [{"var": "occupation, management, business, science, and arts occupations", "yaxis": "Business, Science, and Art", "title": "Occupation"},
                {"var": "occupation, service occupations", "yaxis": "Customer Service"},
                {"var": "occupation, sales and office occupations", "yaxis": "Sales and Office"},
                {"var": "occupation, natural resources, construction, and maintenance occupations", "yaxis": "Construction, Maintenance, and Natural Resources"},
                {"var": "occupation, production, transportation, and material moving occupations", "yaxis": "Production, Transportation, and Moving"}],

        "industry": [{"var": "industry, agriculture, forestry, fishing and hunting, and mining", "yaxis": "Agriculture, Hunting, and Mining", "title": "Industry", "tag": "Blue Collar"},
                {"var": "industry, construction", "yaxis": "Construction", "tag": "Blue Collar"},
                {"var": "industry, manufacturing", "yaxis": "Manufacturing", "tag": "Blue Collar"},
                {"var": "industry, wholesale trade", "yaxis": "Wholesale Trade", "tag": "Blue Collar"},
                {"var": "industry, retail trade", "yaxis": "Retail", "tag": "Service"},
                {"var": "industry, transportation and warehousing, and utilities", "yaxis": "Logistics and Utilities", "tag": "Blue Collar"},
                {"var": "industry, information", "yaxis": "Information Services", "tag": "White Collar"},
                {"var": "industry, finance and insurance, and real estate and rental and leasing", "yaxis": "Finance, Insurance, and Real Estate", "tag": "White Collar"},
                {"var": "industry, professional, scientific, and management, and administrative and waste management services", "yaxis": "Professional Services", "tag": "White Collar"},
                {"var": "industry, educational services, and health care and social assistance", "yaxis": "Healthcare and Education", "tag": "White Collar"},
                {"var": "industry, arts, entertainment, and recreation, and accommodation and food services", "yaxis": "Arts, Hotels, and Dining", "tag": "Service"},
                {"var": "industry, other services, except public administration", "yaxis": "Other", "tag": "Other"},
                {"var": "industry, public administration", "yaxis": "Local Government", "tag": "White Collar"}],
        
        "income": [{"var": "income and benefits (in 2011 inflation-adjusted dollars), median household income (dollars)", "yaxis": "Median Household Income", "title": "Income"},
                {"var": "income and benefits (in 2011 inflation-adjusted dollars), mean household income (dollars)", "yaxis": "Mean Household Income"}],

        "vacancy": [{"var": "housing occupancy, occupied housing units", "yaxis": "Occupied Units", "title": "Housing Vacancy"},
                {"var": "housing occupancy, vacant housing units", "yaxis": "Vacant Units"}],

        "house_value": [{"var": "value, less than $50,000", "yaxis": "<$50,000", "title": "Number of Houses per Value", "tag": "$0-300,000"},
                {"var": "value, $50,000 to $99,999", "yaxis": "$50-90,000", "tag": "$0-300,000"},
                {"var": "value, $100,000 to $149,999", "yaxis": "$100-149,999", "tag": "$0-300,000"},
                {"var": "value, $150,000 to $199,999", "yaxis": "$150-199,999", "tag": "$0-300,000"},
                {"var": "value, $200,000 to $299,999", "yaxis": "$200-299,999", "tag": "$0-300,000"},
                {"var": "value, $300,000 to $499,999", "yaxis": "$300-499,999", "tag": "$300-1,000,000"},
                {"var": "value, $500,000 to $999,999", "yaxis": "$500-999,999", "tag": "$300-1,000,000"},
                {"var": "value, $1,000,000 or more", "yaxis": ">$1,000,000", "tag": "$>1,000,000"}],
                
        "age": [{"var": "sex and age, under 5 years", "yaxis": "<5", "title": "Age in Years", "tag": "Child (0-14)"},
                {"var": "sex and age, 5 to 9 years", "yaxis": "5-9", "tag": "Child (0-14)"},
                {"var": "sex and age, 10 to 14 years", "yaxis": "10-14", "tag": "Child (0-14)"},
                {"var": "sex and age, 15 to 19 years", "yaxis": "15-19", "tag": "Young (14-34)"},
                {"var": "sex and age, 20 to 24 years", "yaxis": "20-24", "tag": "Young (14-34)"},
                {"var": "sex and age, 25 to 34 years", "yaxis": "25-34", "tag": "Young (14-34)"},
                {"var": "sex and age, 35 to 44 years", "yaxis": "35-44", "tag": "Young (14-34)"},
                {"var": "sex and age, 45 to 54 years", "yaxis": "45-54", "tag": "Middle-Aged (35-65)"},
                {"var": "sex and age, 55 to 59 years", "yaxis": "55-59", "tag": "Middle-Aged (35-65)"},
                {"var": "sex and age, 60 to 64 years", "yaxis": "60-64", "tag": "Middle-Aged (35-65)"},
                {"var": "sex and age, 65 to 74 years", "yaxis": "65-74", "tag": "Elderly (65+)"},
                {"var": "sex and age, 75 to 84 years", "yaxis": "75-84", "tag": "Elderly (65+)"},
                {"var": "sex and age, 85 years and over", "yaxis": ">84", "tag": "Elderly (65+)"}]        
    }

    if year_len > 1:
        if any("tag" in x for x in data[arg]):
            tags = []
            
            for i in data[arg]:
                if "title" in i:
                    title = i.get("title")
                var = i.get("var", None)
                tag = i.get("tag")
                new_df.rename(columns={var:tag}, inplace=True)
                if tag not in tags:
                    tags.append(tag)

            for tag in tags:
                if (new_df.columns == tag).sum() > 1:
                    values = new_df[tag].sum(axis=1)
                    new_df = new_df.drop(columns=tag)
                    new_df[tag] = values
            new_df = new_df.loc[:, ~new_df.columns.duplicated(keep="first")]
            for z, tag in enumerate(tags):
                yaxis = tag
                var = tags[z]
                if z == 0:
                    plot = line(new_df, var, yaxis, title)
                else:
                    plot = new_line(plot, new_df, var, yaxis)
            plot_html = plot.to_html(full_html=False, include_plotlyjs='cdn',div_id=None)
            
        else:
            for i in data[arg]:
                var = i.get("var", None)
                title = i.get("title", None)
                yaxis = i.get("yaxis", None)
                
                if title != None:
                    plot = line(new_df, var, yaxis, title)
                else:
                    plot = new_line(plot, new_df, var, yaxis)
                    
            plot_html = plot.to_html(full_html=False, include_plotlyjs='cdn',div_id=None)
            
    else:
        for i in data[arg]:
            var = i.get("var", None)
            yaxis = i.get("yaxis", None)
            title = i.get("title", None)
            
            if title != None:
                plot = bar(new_df, var, yaxis, title)
            else: 
                plot = new_bar(plot, new_df, var, yaxis)
                
        plot_html = plot.to_html(full_html=False, include_plotlyjs='cdn',div_id=None)
    return plot_html

if __name__ == "__main__":
    visualize(arg, year_len, new_df)