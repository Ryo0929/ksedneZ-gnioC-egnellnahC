from dash import dash_table
from dash import dcc
from dash import html

def generate_table_layout(df,page_size=25,hidden_columns=[],ticket_id=None):
    return html.Div([
        dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        page_action='native',
        page_current= 0,
        page_size= page_size,
        hidden_columns=hidden_columns,
        css=[{"selector": ".show-hide", "rule": "display: none"}]
        ),
        html.Label(
            'No result matched',
            id='result_label',
            hidden= True),
        dcc.Input(
            id='ticket_id',
            placeholder="search by id",
        )
    ])
def generate_error_layout():
    return html.Div([
        html.Label(
            'Sorry, the API is unavailable or the response is invalid',
            id='result_label',
            ),
    ])