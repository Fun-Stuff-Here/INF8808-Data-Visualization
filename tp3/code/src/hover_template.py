'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
 
    hover_template = '<span style="font-weight:bold; font-family:Roboto Slab; color:Black">Neighbourhood : </span>' 
    hover_template +='<span style="font-weight:regular; font-family:Roboto Slab; color:Black">%{y}</span><br>'
    hover_template += '<span style="font-weight:bold; font-family:Roboto Slab; color:Black">Year : </span>' 
    hover_template +='<span style="font-weight:regular; font-family:Roboto Slab; color:Black">%{x}</span><br>'
    hover_template += '<span style="font-weight:bold; font-family:Roboto Slab; color:Black">Trees Planted : </span>' 
    hover_template +='<span style="font-weight:regular; font-family:Roboto Slab; color:Black">%{z}</span><br>'
    hover_template += '<extra></extra>'

    # TODO : Define and return the hover template
    return hover_template

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template

    hover_template = '<span style="font-weight:bold; font-family:Roboto Slab; color:Black">Date : </span>' 
    hover_template +='<span style="font-weight:regular; font-family:Roboto Slab; color:Black">%{y}</span><br>'
    hover_template += '<span style="font-weight:bold; font-family:Roboto Slab; color:Black">Trees : </span>' 
    hover_template +='<span style="font-weight:regular; font-family:Roboto Slab; color:Black">%{x}</span><br>'
    hover_template += '<extra></extra>'

    return hover_template

