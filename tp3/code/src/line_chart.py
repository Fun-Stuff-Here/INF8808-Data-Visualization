'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.
        This empty version of the line chart should contain an informational
        message and a grey rectangle as a background

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    text = 'No data to display. Select a cell in the heatmap for more information.'
    #create an empty figure wit scale 0 to 1
    fig = go.Figure()
    #add the text to the figure to the center add word wrap
    fig.add_annotation(text=text, x=0.5, y=0.5,xref='paper',yref='paper', showarrow=False, font_size=10,
    xanchor='center', yanchor='middle', align='center',
    )

    fig.update_layout(dragmode= False, xaxis_visible=False, yaxis_visible=False)
    add_rectangle_shape(fig)
    return fig


def add_rectangle_shape(fig: go.Figure):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    fig.add_shape(type="rect",
        x0=0,
        y0=0.25,
        x1=1,
        y1=0.75,
        xref="paper",
        yref="paper",
        ysizemode="scaled",
        xsizemode="scaled",
        fillcolor=THEME["pale_color"],
        line = dict(color=THEME["pale_color"], width=0),
    )
    return fig


def get_figure(line_data:pd.DataFrame, arrond:str, year:int):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template
    
    if line_data.empty:
        return get_empty_figure()

    title = f'Trees planted in {arrond} in {year}'

    if len(line_data) == 1:
        return px.scatter(line_data,x='Date_Plantation', y= 'Counts',title=title)
    fig = px.line(line_data,x='Date_Plantation', y= 'Counts',title=title)
    return fig
