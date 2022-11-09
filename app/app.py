import json

import cfunits
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Row(
    dbc.Col(
        html.Div(
            [
                dcc.Location(id="url_location"),
                html.Br(),
                html.H3("UDUNITS Lookup"),
                html.H5("Check to see if your unit is valid. (Case sensitive)"),
                dbc.Input(
                    id="input_text",
                    size="lg",
                    className="mb-3",
                    type="text",
                    placeholder="eg: kilometers",
                ),
                html.Br(),
                html.H6(id="output"),
                dcc.Download(id="download_result"),
            ],
            style={"margin": "30px", "padding": "40px"},
        ),
    ),
)


server = app.server


@app.callback(
    Output("input_text", "value"),
    Input("url_location", "pathname"),
    Input("url_location", "search"),
)
def get_units_from_url(pathname, unit):
    if unit:
        return unit[1:]


@app.callback(
    Output("download_result", "data"),
    Input("url_location", "pathname"),
    Input("url_location", "search"),
)
def test_units(pathname, input_text):
    if input_text is None:
        return
    unit = cfunits.Units(input_text)
    if pathname == "/json":
        unit = cfunits.Units(input_text[1:])
        return dict(
            content=json.dumps(
                {
                    "is_valid": unit.isvalid,
                    "formatted": unit.formatted(names=True, definition=True),
                    "original_format": input_text[1:],
                }
            ),
            filename="udunit.json",
        )


@app.callback(
    Output("output", "children"),
    Input("input_text", "value"),
)
def cb_render(input_text):
    if input_text:
        units = cfunits.Units(input_text)
        if units.isvalid:
            return html.H3(
                dbc.Alert(
                    f"{input_text}: {units.formatted(names=True, definition=True)}",
                    color="success",
                    className="me-1",
                )
            )
        return (
            html.H3(dbc.Alert("Not a valid UDUNIT", color="danger", className="me-1")),
        )


if __name__ == "__main__":
    app.run_server(debug=True)
