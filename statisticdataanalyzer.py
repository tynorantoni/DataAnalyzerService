import json

import pandas as pd

def make_basic_anal(city, data_from_db):
    data_dict = {}
    df = pd.DataFrame(data_from_db).dropna()
    data_dict['avg']= df.mean
    data_dict['median']= df.median
    data_dict['sd']= df.std
    data_dict['min']= df.min
    data_dict['max']= df.max

    basic_stat_data= json.loads(data_dict)

    return '{}:{}'.format(city, basic_stat_data)




