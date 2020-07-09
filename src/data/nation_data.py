from src.data import dataverse
import os
import pandas as pd
from pandas_profiling import ProfileReport

def download():
    ref = 'doi:10.7910/DVN/BMRPVH/SPI1XO'
    filename = 'nation_data.tab'
    status, headers, encoding = dataverse.download(ref, filename)
    return status, headers, encoding


def profile():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    filename = '../../data/external/nation_data.tab'
    df = pd.read_csv(filename, sep='\t', lineterminator='\n')
    return ProfileReport(df, title="Nation Data Minimal Profile", minimal=True, html={'style': {'full_width': True}})
