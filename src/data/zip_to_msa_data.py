import os
import requests


def download():
    print('Beginning ZCTA to MSA download with requests')

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    url = 'https://www2.census.gov/geo/docs/maps-data/data/rel/zcta_cbsa_rel_10.txt'
    filename = '../../data/external/zip_to_msa.csv'
    r = requests.get(url)
    r.raise_for_status()

    with open(filename, 'wb') as f:
        f.write(r.content)

    return r.status_code, r.headers['content-type'], r.encoding
