# start with hard cvs to test
# script to present requested visualizations
# time series, geographic ancestry, etc.
# These will be sent back to front-end

import plotly.express as px
import pandas as pd

def line(new_df, var, yaxis, title = None):
    if title == None:
        title = yaxis
    plot = px.line(
        new_df, x = new_df.index, y = var,
        title = f"{title} per Year",
        markers = True)
    plot.update_traces(
        name = yaxis, showlegend = True)
    plot.update_layout(
        xaxis_title="Year",
        yaxis_title=f"{yaxis}",
        xaxis = dict(
            tickmode='linear', 
            gridcolor='lightgray',
            dtick=1),
        yaxis = dict(
            gridcolor='lightgray'),
        yaxis_autorange=True,       
        plot_bgcolor='white')
    return plot

def new_line(plot, new_df, var, yaxis):
    plot.add_scatter(
        x = new_df.index, y = new_df[var], 
        mode = 'lines+markers',
        name = yaxis)
    plot.update_layout(yaxis_autorange=True)
    return plot

def hist(fix):
    return

def visualize(arg, new_df): 
    # List of variables for plots
    functions = {
        "housing": [{"var": "households by type, total households", "yaxis": "Total Households", "tag": "base"},
                    {"var": "households by type, average family size", "yaxis": "Average Family Size", "tag": "base"},
                    {"var": "relationship, population in households", "yaxis": "Total Population", "tag": "base"}],
        "education": [{"var": "educational attainment, high school graduate (includes equivalency)", "yaxis": "High School", "tag": "base_edu", "title": "Educational Attainment"},
        	        {"var": "educational attainment, associate's degree", "yaxis": "Associate's Degree", "tag": "edu"},
                    {"var": "educational attainment, bachelor's degree", "yaxis": "Bachelor's Degree", "tag": "edu"},
                    {"var": "educational attainment, graduate or professional degree", "yaxis": "Graduate Degree", "tag": "edu"}],
        "culture": {},
        "employment": {},
        "economic": {},
        "demographic": {}
    }
    # Return parameters 
    for i in functions[arg]:
        var = i["var"]
        yaxis = i["yaxis"]
        title = i.get("title", None)
        tag = i["tag"]
        if "base" in tag:
            plot = line(new_df, var, yaxis, title)
        else:
            plot = new_line(plot, new_df, var, yaxis)
    plot.show()

# If single year is chosen, switch to histogram/bar chart.   
if __name__ == "__main__":
    visualize(arg, new_df)