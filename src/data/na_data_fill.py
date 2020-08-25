import os
import pandas as pd
from pandas_profiling import ProfileReport


def profile():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    filename = '../../data/processed/na-data-fill.csv'
    df = pd.read_csv(filename)
    return ProfileReport(df, title="Clean Data with NA Data Filled Profile",
                         html={'style': {'full_width': True}})
