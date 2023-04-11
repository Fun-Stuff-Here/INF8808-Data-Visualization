"""
    This file contains the functions to call when
    a click is detected on the map, depending on the context
"""
import dash_html_components as html


def no_clicks(style):
    """
    Deals with the case where the map was not clicked

    Args:
        style: The current display style for the panel
    Returns:
        title: The updated display title
        mode: The updated display title
        theme: The updated display theme
        style: The updated display style for the panel
    """
    # TODO : Handle no clicks on the map
    if style["visibility"] == "hidden":
        return None, None, None, style
    return None, None, None, {"visibility": "hidden"}


def map_base_clicked(title, mode, theme, style):
    """
    Deals with the case where the map base is
    clicked (but not a marker)

    Args:
        title: The current display title
        mode: The current display title
        theme: The current display theme
        style: The current display style for the panel
    Returns:
        title: The updated display title
        mode: The updated display title
        theme: The updated display theme
        style: The updated display style for the panel
    """
    # TODO : Handle clicks on the map base
    if style["visibility"] == "hidden":
        return None, None, None, style
    return title, mode, theme, style


def map_marker_clicked(
    figure, curve, point, title, mode, theme, style
):  # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    """
    Deals with the case where a marker is clicked

    Args:
        figure: The current figure
        curve: The index of the curve containing the clicked marker
        point: The index of the clicked marker
        title: The current display title
        mode: The current display title
        theme: The current display theme
        style: The current display style for the panel
    Returns:
        title: The updated display title
        mode: The updated display title
        theme: The updated display theme
        style: The updated display style for the panel
    """
    # TODO : Handle clicks on the markers

    title = [
        html.Span(
            figure["data"][curve]["customdata"][point][0],
            style={
                "color": figure["data"][curve]["marker"]["color"],
                "fontWeight": "bold",
            },
        )
    ]

    mode = [
        html.Span(
            figure["data"][curve]["customdata"][point][2], style={"fontWeight": "bold"}
        ),
        html.Div("\n"),
    ]
    
    style = {"visibility": "visible", "border": "1px solid black", "padding": "10px"}
    theme = None
    if figure["data"][curve]["customdata"][point][1]:
        themes = list(figure["data"][curve]["customdata"][point][1].split("\n"))
        theme = [
            html.Div("Thématique:"),
            html.Ul(children=[html.Li(l) for l in themes]),
        ]

    return (
        title,
        mode,
        theme,
        style,
    )
