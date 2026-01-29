import plotly.express as px
import pandas as pd
pd.options.mode.chained_assignment = None


# Create new line graph (for multi-year requests) with dynamic range
def line(new_df, var, yaxis, title = None):
    if title == None:
        title = yaxis
    plot = px.line(new_df, x = new_df.index, y = var, title = f"{title} per Year", markers = True)
    plot.update_traces(name = yaxis, showlegend = True)
    plot.update_layout(xaxis_title = "Year", yaxis_title = f"{title}", xaxis = dict(tickmode = 'linear', gridcolor = 'lightgray', dtick = 1),
        yaxis = dict(gridcolor = 'lightgray'), yaxis_autorange = True, plot_bgcolor='white')
    return plot


# Add new lines based on selected variable
def new_line(plot, new_df, var, yaxis):
    plot.add_scatter(x = new_df.index, y = new_df[var], mode = 'lines+markers', name = yaxis)
    plot.update_layout(yaxis_autorange=True)
    return plot


# Create new bar graph (for one-year requests) with dynamic range
def bar(new_df, var, yaxis, title = None):
    if title == None:
        title = yaxis
    year = new_df.index[0]
    plot = px.bar(data_frame = new_df, x = new_df.index, y = var, title = f"{title} in {year}", color_continuous_scale = "Viridis")
    plot.update_traces(width = 0.4, opacity = 0.8, showlegend = True, name = yaxis)
    plot.update_layout(xaxis = dict(type = 'category', tickmode = 'array'), yaxis_title = title, xaxis_title = "Year", barmode = "group")
    return plot


# Add new bars as applicable 
def new_bar(plot, new_df, var, yaxis):
    plot.add_bar(x=new_df.index, y=new_df[var], name=yaxis)
    plot.update_layout(barmode="group")
    plot.update_traces(width = None)
    return plot



def visualize(arg, year_len, new_df, data): 
    # Selector function to route request to correct graph-maker function
    # Multi-year requests
    if year_len > 1:
        # Variables with tags
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
        
        # Variables without tags
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
    
    # Single-year requests - no grouping needed as visuals support complexity 
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