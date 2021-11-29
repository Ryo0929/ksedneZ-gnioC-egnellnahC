import json
import requests
import pandas as pd

def get_data(domain,account,password):
    url='https://'+domain+'.zendesk.com/api/v2/tickets.json'
    response = requests.get(url,auth=(account,password))
    if response.status_code==200:
        json_data = json.loads(response.text)
        if 'tickets'not in json_data.keys():
            return None
        df=pd.json_normalize(json_data['tickets'])
        return df
    else:
        return None