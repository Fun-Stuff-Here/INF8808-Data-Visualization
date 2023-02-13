'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
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
    fig = px.line(x=[0], y=[0], title='No data to display. Select a cell in the heatmap for more information.')
    fig.update_layout(dragmode=False)
    return fig


def add_rectangle_shape(fig):
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
        x0=0, y0=0.25, x1=1, y1=0.75,
        line_color=THEME["pale_color"],
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
    fig = px.line(line_data,x='Date_Plantation', y= 'Counts',title=f'{arrond} - {year}')
    return fig
