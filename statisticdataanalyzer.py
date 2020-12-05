import json

import pandas as pd
import numpy as np


# making an analysis of given dataset from db
def make_basic_anal(data_from_db):
    df = pd.DataFrame(data_from_db).dropna().rename(columns={0: 'Index', 1: 'Date', 2: 'Street', 3: 'Cyclists'})
    df['Cyclists'] = df['Cyclists'].astype(float)
    pivoted = pd.pivot_table(df, index=['Date'], columns=['Street'], values='Cyclists', aggfunc=np.average)
    stat_dict = {}

    for col in pivoted.columns:
        stat_dict[col] = {}
        stat_dict[col]['avg'] = pivoted[col].mean()
        stat_dict[col]['dev'] = pivoted[col].std()
        stat_dict[col]['max'] = pivoted[col].max()
        stat_dict[col]['min'] = pivoted[col].min()
        stat_dict[col]['median'] = pivoted[col].median()

    return json.dumps(stat_dict)


# returns json ready to parse into a chart
def prepare_data_for_chart(data_from_db):
    df = pd.DataFrame(data_from_db).dropna().rename(columns={0: 'Index', 1: 'Date', 2: 'Street', 3: 'Cyclists'})
    df['Cyclists'] = df['Cyclists'].astype(float)
    pivoted = pd.pivot_table(df, index=['Date'], columns=['Street'], values='Cyclists', aggfunc=np.average)
    data_from_all_counters = {}

    for col in pivoted.columns:
        data_list = []
        row_no = 0
        for row in pivoted[col]:
            data_list.append((str(pivoted.index[row_no]), int(row)))
            row_no += 1
        data_from_all_counters[col] = data_list

    return json.dumps(json.dumps(data_from_all_counters))
