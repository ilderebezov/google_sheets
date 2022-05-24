from dash import Dash, dash_table, dcc, html
from src.graph.graph_data import plot

app = Dash(__name__)


def serve_layout():
    """
    Form output page
    :return:
    html page
    """

    df_graph = plot()[1].sort_values('№')
    return html.Div(children=[
        html.H1(children='Каналсервис'),

        html.Div(children='''
            Plot and table.
        '''),

        dcc.Graph(
            id='example-graph x**2',
            figure=plot()[0],
        ),

        dash_table.DataTable(df_graph.to_dict('records'), [{"name": i, "id": i} for i in df_graph.columns]),

        ]
    )

app.layout = serve_layout
