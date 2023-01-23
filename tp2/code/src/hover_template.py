'''
    Provides the template for the hover tooltips.
'''
from modes import MODES, MODE_TO_COLUMN
import pandas as pd


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating player name with:
                - Font family: Grenze Gotisch
                - Font size: 24px
                - Font color: Black
            * The number of lines spoken by the player, formatted as:
                - The number of lines if the mode is 'Count ("X lines").
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent' ("Y% of lines").

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements descibed above
    '''
    # TODO: Generate and return the over template# value of y
        
    hover_template = '<span><b style="font-size:24px;font-family:Grenze Gotisch;color:Black;"></b>{Name}</span><br>'.format(Name=name) 
    # access Y values with hover 
    hover_template += '%{y}'
    if mode == MODES['count']:
        hover_template += '<b style="font-size:15px;font-family:Arial;color:Grey;"> lines</b>'   
        hover_template += '<extra></extra>'

    else:
        hover_template += '<b style="font-size:15px;font-family:Arial;color:Grey;"> % of lines</b>'
        hover_template += '<extra></extra>'
    return hover_template


