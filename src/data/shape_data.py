import pandas as pd
import numpy as nd


def fill_years(df):
    years = pd.DataFrame(range(1988, 2017))
    years.columns = ['year']
    unique = df.zipcode.unique()
    result = pd.DataFrame()
    for zipcode in unique:
        append = years.copy()
        state = df.loc[df['zipcode'] == zipcode, 'state'].iloc[0]
        append['zipcode'] = zipcode
        append['state'] = state
        result = pd.concat([result, append], ignore_index=True)
    return result
