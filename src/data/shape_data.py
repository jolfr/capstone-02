import pandas as pd
import numpy as nd


def generate_filled(df):
    years = pd.DataFrame(range(1988, 2017))
    years.columns = ['year']
    unique = df.zipcode.unique()
    result = pd.DataFrame()
    for zipcode in unique:
        append = years.copy()
        append['zipcode'] = zipcode
        result = pd.concat([result, append], ignore_index=True)
    return result
