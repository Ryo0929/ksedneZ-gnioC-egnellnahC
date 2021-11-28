import sys
import dash
from dash.dependencies import Input, Output
from model import *
from view import *

def main(domain,account,password):
    # columns that would be hidden when list all tickets
    hidden_columns=["url","external_id","updated_at","type","raw_subject","description","priority","status","recipient",
        'organization_id', 'group_id', 'collaborator_ids', 'follower_ids',
        'email_cc_ids', 'forum_topic_id', 'problem_id', 'has_incidents',
        'is_public', 'due_at', 'tags', 'custom_fields', 'satisfaction_rating',
        'sharing_agreement_ids', 'fields', 'followup_ids', 'ticket_form_id',
        'brand_id', 'allow_channelback', 'allow_attachments', 'via.channel',
        'via.source.rel',"submitter_id","assignee_id"]
    # columns that would be hidden when list one tickets
    not_hidden_columns=[x for x in hidden_columns if x not in ["description"]]

    app = dash.Dash(__name__)
    df=get_data(domain,account,password)
    layout=None
    if df is None:
        layout=generate_error_layout()
    else:
        layout=generate_table_layout(df,25,hidden_columns)

    app.layout = layout
    
    #When user input in the text box, table data, table columns and/or result label would changed correspondetly.
    @app.callback(
        [Output("table", "data"),Output("table", "hidden_columns"),Output("result_label", "hidden")],
        [Input("ticket_id", "value")]
    )
    def updateTable(val):
        try:
            result=df[df["id"]==int(val)]
            if len(result.index)==0:
                return result.to_dict("records"),not_hidden_columns,False
            else:
                return result.to_dict("records"),not_hidden_columns,True
        except:
            return df.to_dict("records"),hidden_columns,True
    app.run_server(debug=False)

if __name__ == '__main__':
    domain = sys.argv[1]
    account = sys.argv[2]
    password = sys.argv[3]
    
    main(domain,account,password)