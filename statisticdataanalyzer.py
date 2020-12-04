import json

import pandas as pd
import numpy as np
from dbmanipulation import select_data_from_city


def make_basic_anal(city, data_from_db):

    df = pd.DataFrame(data_from_db).dropna().rename(columns={0:'Index',1:'Date',2:'Street',3:'Cyclists'})
    df['Cyclists'] = df['Cyclists'].astype(float)
    pivoted = pd.pivot_table(df, index=['Date'],columns=['Street'],values='Cyclists',aggfunc=np.sum)




    # data_dict['avg'] = df.mean
    # data_dict['median'] = df.median
    # data_dict['sd'] = df.std
    # data_dict['min'] = df.min
    # data_dict['max'] = df.max

    # basic_stat_data = json.dumps(data_dict)
    #
    return '{}:{}'.format(city, data_dict)


make_basic_anal('krakow', select_data_from_city('krk','2020-09-01','2020-09-10'))