import json
import requests
import pandas as pd

def get_data(domain,account,password):
    response = requests.get(domain,auth=(account,password))
    if response.status_code==200:
        json_data = json.loads(response.text)
        df=pd.json_normalize(json_data['tickets'])
        return df
    else:
        return None